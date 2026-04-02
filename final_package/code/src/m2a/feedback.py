from __future__ import annotations

from .schemas import VerificationResult


def evaluate_progress(task_spec, state, stage: str) -> VerificationResult:
    checks: dict[str, bool] = {}
    blocking: list[str] = []
    non_blocking: list[str] = []
    evidence_refs = [paper["citation_id"] for paper in state.external_state["read_papers"]]

    checks["boundary_respected"] = not task_spec.boundary_topics or state.external_state["boundary_note_emitted"]
    if task_spec.boundary_topics and not state.external_state["boundary_note_emitted"]:
        blocking.append("boundary: request includes deferred topics and requires a boundary note")

    checks["ambiguity_resolved"] = not task_spec.ambiguity_flags or state.external_state["clarification_emitted"]
    if task_spec.ambiguity_flags and not state.external_state["clarification_emitted"]:
        blocking.append("goal: unresolved ambiguity prevents a bounded review")

    read_papers = state.external_state["read_papers"]
    read_count = len(read_papers)
    checks["paper_budget_met"] = read_count >= task_spec.paper_budget_min or stage == "final" and bool(state.external_state["review_sources"])
    if stage != "final" and read_count < task_spec.paper_budget_min and not task_spec.ambiguity_flags and not task_spec.boundary_topics:
        blocking.append(f"grounding: only {read_count} papers read; need at least {task_spec.paper_budget_min}")

    covered_topics = set(state.external_state["review_covered_topics"] if stage == "final" else [topic for paper in read_papers for topic in paper["topic_tags"]])
    missing_topics = [topic for topic in task_spec.requested_topics if topic not in covered_topics]
    checks["topic_coverage"] = not missing_topics
    if missing_topics:
        blocking.append("planning: missing topic coverage for " + ", ".join(missing_topics))

    if stage == "final":
        citations = state.external_state["final_citations"]
        checks["citations_present"] = len(citations) >= min(task_spec.paper_budget_min, max(1, len(task_spec.requested_topics)))
        if not checks["citations_present"]:
            blocking.append("grounding: final review lacks sufficient citations")
        checks["comparison_present"] = (not task_spec.comparison_mode) or state.external_state["comparison_done"]
        if task_spec.comparison_mode and not state.external_state["comparison_done"]:
            blocking.append("goal: comparison requested but output does not compare alternatives")
        checks["recommendation_present"] = (not task_spec.recommendation_required) or state.external_state["recommendation_made"]
        if task_spec.recommendation_required and not state.external_state["recommendation_made"]:
            blocking.append("goal: recommendation requested but output does not defend one")
        if state.external_state["used_stale_memory"]:
            blocking.append("memory: stale memory influenced the draft without fresh verification")
    else:
        checks["citations_present"] = True
        checks["comparison_present"] = True
        checks["recommendation_present"] = True

    satisfied = not blocking and all(checks.values())
    return VerificationResult(
        step=state.step,
        stage=stage,
        satisfied=satisfied,
        checks=checks,
        blocking_issues=blocking,
        non_blocking_issues=non_blocking,
        evidence_refs=evidence_refs,
    )


def reflection_actions(verification: VerificationResult, critique: str = "") -> list[str]:
    if not verification.blocking_issues:
        return []
    actions: list[str] = []
    for issue in verification.blocking_issues:
        if issue.startswith("planning: missing topic coverage for "):
            topics = issue.removeprefix("planning: missing topic coverage for ")
            actions.extend(f"search:{topic.strip()}" for topic in topics.split(",") if topic.strip())
        elif issue.startswith("goal: unresolved ambiguity"):
            actions.append("clarify")
        elif issue.startswith("boundary:"):
            actions.append("handoff_boundary")
        elif issue.startswith("grounding: only"):
            actions.append("read_more")
    if critique and not actions:
        return []
    return list(dict.fromkeys(actions))


def diagnose_failure(result, verification: VerificationResult) -> list[str]:
    diagnoses: list[str] = []
    for issue in verification.blocking_issues:
        if issue.startswith("goal:"):
            diagnoses.append("goal")
        elif issue.startswith("planning:"):
            diagnoses.append("planning")
        elif issue.startswith("memory:"):
            diagnoses.append("memory")
        elif issue.startswith("grounding:"):
            diagnoses.append("grounding")
        elif issue.startswith("boundary:"):
            diagnoses.append("stop")
    if result.variant == "model_only":
        diagnoses.append("action")
    if verification.blocking_issues and result.stop_decision.outcome in {"clarification_needed", "handoff"}:
        diagnoses.append("stop")
    return list(dict.fromkeys(diagnoses))
