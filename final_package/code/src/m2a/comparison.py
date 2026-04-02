from __future__ import annotations

from pathlib import Path

from .artifacts import emit_comparison_artifacts, emit_run_artifacts
from .control import VALID_VARIANTS, run_variant
from .feedback import diagnose_failure
from .schemas import ArchitectureAssessment


def _assess(task_spec, result) -> ArchitectureAssessment:
    tool_calls = len(result.tool_observations)
    papers_read = len(result.run_summary.get("read_papers", []))
    citations_used = len(result.run_summary.get("final_citations", []))
    memory_events = sum(1 for event in result.memory_log if event.event_type in {"seed", "write", "retrieve", "forget"})
    reflection_events = len(result.run_summary.get("reflection_actions", []))
    verification = result.verification_results[-1]
    diagnoses = diagnose_failure(result, verification)
    used_tools = sorted({observation.tool_name for observation in result.tool_observations})
    if result.stop_decision.outcome == "success":
        notes = "Met the final success criteria."
    else:
        notes = "; ".join(result.stop_decision.remaining_blockers) or "Stopped without success."
    return ArchitectureAssessment(
        variant=result.variant,
        outcome=result.stop_decision.outcome,
        success=result.stop_decision.outcome == "success",
        tool_calls=tool_calls,
        papers_read=papers_read,
        citations_used=citations_used,
        memory_events=memory_events,
        reflection_events=reflection_events,
        used_tools=used_tools,
        diagnoses=diagnoses,
        blocking_issues=list(result.stop_decision.remaining_blockers),
        notes=notes,
    )


def _assessment_score(task_spec, assessment: ArchitectureAssessment) -> int:
    score = 0
    if assessment.success:
        score += 10
    elif assessment.outcome in {"clarification_needed", "handoff"} and (task_spec.ambiguity_flags or task_spec.boundary_topics):
        score += 4
    score += assessment.citations_used
    score += min(assessment.papers_read, task_spec.paper_budget_max)
    score += assessment.reflection_events
    score -= len(assessment.blocking_issues)

    used_tools = set(assessment.used_tools)
    multi_topic_comparison = len(task_spec.requested_topics) >= 3 and task_spec.comparison_mode
    if multi_topic_comparison and assessment.success:
        if {"search_corpus", "write_note"} <= used_tools:
            score += 3
        elif "search_corpus" in used_tools or "write_note" in used_tools:
            score += 1
    if task_spec.paper_budget_max <= 2 and assessment.variant == "scripted_pipeline" and assessment.success:
        score += 3
    if task_spec.paper_budget_max <= 2 and assessment.variant in {"memory_rich_tool_poor", "capstone_agent"} and assessment.success:
        score -= 2
    if task_spec.boundary_topics:
        score -= 100
    return score


def _render_matrix(task_spec, assessments: list[ArchitectureAssessment]) -> str:
    lines = [
        f"# Architecture Comparison Matrix: {task_spec.request_id}",
        "",
        "| Variant | Outcome | Tool calls | Papers read | Citations | Memory events | Reflection events | Diagnoses |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for assessment in assessments:
        lines.append(
            f"| {assessment.variant} | {assessment.outcome} | {assessment.tool_calls} | {assessment.papers_read} | {assessment.citations_used} | {assessment.memory_events} | {assessment.reflection_events} | {', '.join(assessment.diagnoses) or 'none'} |"
        )
    return "\n".join(lines)


def _render_recommendation(task_spec, assessments: list[ArchitectureAssessment]) -> str:
    ranked = sorted(assessments, key=lambda item: (_assessment_score(task_spec, item), item.variant), reverse=True)
    best = ranked[0]
    if task_spec.boundary_topics:
        lines = [f"# Fit Recommendation: {task_spec.request_id}", "", "Recommended variant: `none_in_scope`", "", "No in-scope architecture should be recommended here because the request is dominated by explicitly deferred topics."]
    else:
        lines = [f"# Fit Recommendation: {task_spec.request_id}", "", f"Recommended variant: `{best.variant}`", ""]
        if best.success:
            lines.append(f"`{best.variant}` is recommended because it achieved a successful bounded outcome with {best.citations_used} citations across {best.papers_read} paper reads.")
        else:
            lines.append(f"No variant achieved full success. `{best.variant}` is still the best bounded choice because it handled the task more safely than the alternatives.")
    lines.extend(["", "## Evidence from observed runs", ""])
    for assessment in ranked:
        tool_summary = ", ".join(assessment.used_tools) or "no tools"
        lines.append(f"- `{assessment.variant}` -> {assessment.outcome}: {assessment.notes} Tool profile observed: {tool_summary}.")
    if task_spec.paper_budget_max <= 2:
        lines.extend(["", "## Small-task note", "", "This task is deliberately small. The recommendation therefore penalizes unnecessary control overhead when simpler variants already succeed."])
    return "\n".join(lines)


def _render_failure_diagnosis(task_spec, assessments: list[ArchitectureAssessment]) -> str:
    lines = [f"# Failure Diagnosis: {task_spec.request_id}", "", "## Variant-by-variant diagnosis", ""]
    for assessment in assessments:
        if assessment.success:
            lines.append(f"- `{assessment.variant}` succeeded. Dominant diagnosis: none.")
        else:
            lines.append(f"- `{assessment.variant}` failed with diagnoses `{', '.join(assessment.diagnoses) or 'uncategorized'}` and blockers: {', '.join(assessment.blocking_issues) or 'none recorded'}.")
    lines.extend(["", "## Cross-variant misconceptions surfaced", ""])
    lines.extend(
        [
            "- Tool calls do not imply task success; some variants found papers but still failed final verification.",
            "- More memory is not always better; stale recall can create a memory-specific blocker.",
            "- Planning earns its keep only when it changes evidence collection or stop behavior.",
        ]
    )
    return "\n".join(lines)


def _render_boundary_note(task_spec, assessments: list[ArchitectureAssessment]) -> str | None:
    if not task_spec.boundary_topics:
        return None
    lines = [f"# Boundary Note: {task_spec.request_id}", "", "The request crossed explicit repository boundaries and is therefore deferred.", "", "## Deferred topics", ""]
    for topic in task_spec.boundary_topics:
        lines.append(f"- {topic}")
    lines.extend(["", "## Observed outcome", ""])
    for assessment in assessments:
        lines.append(f"- `{assessment.variant}` -> {assessment.outcome}")
    lines.extend(["", "This repository deliberately stops here instead of simulating RL control, IR internals, live retrieval, symbolic planning formalisms, or production operations."])
    return "\n".join(lines)


def compare_architectures(task_spec, out_dir: str | Path, variants: list[str] | None = None) -> dict[str, object]:
    chosen = list(variants or VALID_VARIANTS)
    for variant in chosen:
        if variant not in VALID_VARIANTS:
            raise ValueError(f"Unsupported variant: {variant}")
    base_dir = Path(out_dir)
    variant_dir = base_dir / "variants"
    assessments: list[ArchitectureAssessment] = []
    for variant in chosen:
        result = run_variant(task_spec, variant, variant_dir / variant)
        emit_run_artifacts(result, variant_dir / variant)
        assessments.append(_assess(task_spec, result))
    matrix_md = _render_matrix(task_spec, assessments)
    recommendation_md = _render_recommendation(task_spec, assessments)
    failure_md = _render_failure_diagnosis(task_spec, assessments)
    boundary_md = _render_boundary_note(task_spec, assessments)
    emit_comparison_artifacts(base_dir, matrix_md, recommendation_md, failure_md, boundary_md)
    return {
        "assessments": assessments,
        "comparison_matrix_md": matrix_md,
        "fit_recommendation_md": recommendation_md,
        "failure_diagnosis_md": failure_md,
        "boundary_note_md": boundary_md,
    }
