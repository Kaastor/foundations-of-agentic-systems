from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any

from .schemas import HandoffNote, RunResult, TaskSpec


def _jsonable(value: Any) -> Any:
    if is_dataclass(value):
        return asdict(value)
    if isinstance(value, dict):
        return {key: _jsonable(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_jsonable(item) for item in value]
    return value


def ensure_dir(path: str | Path) -> Path:
    target = Path(path)
    target.mkdir(parents=True, exist_ok=True)
    return target


def read_json(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path: str | Path, value: Any) -> None:
    Path(path).write_text(json.dumps(_jsonable(value), indent=2, sort_keys=False) + "\n", encoding="utf-8")


def write_jsonl(path: str | Path, rows: list[Any]) -> None:
    lines = [json.dumps(_jsonable(row), sort_keys=False) for row in rows]
    Path(path).write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def write_text(path: str | Path, text: str) -> None:
    Path(path).write_text(text.rstrip() + "\n", encoding="utf-8")


def load_task_spec(path: str | Path) -> TaskSpec:
    return TaskSpec.from_dict(read_json(path))


def render_task_spec_markdown(spec: TaskSpec) -> str:
    def section(title: str, items: list[str]) -> str:
        lines = [f"## {title}", ""]
        if items:
            lines.extend(f"- {item}" for item in items)
        else:
            lines.append("- None")
        return "\n".join(lines)

    parts = [
        f"# Task Spec: {spec.request_id}",
        "",
        "## Request",
        "",
        spec.raw_request.strip(),
        "",
        "## Structured fields",
        "",
        f"- Paper budget: {spec.paper_budget_min} to {spec.paper_budget_max}",
        f"- Comparison mode: {spec.comparison_mode}",
        f"- Recommendation required: {spec.recommendation_required}",
        f"- Max steps: {spec.max_steps}",
        "",
        section("Goals", spec.goals),
        "",
        section("Constraints", spec.constraints),
        "",
        section("Subgoals", spec.subgoals),
        "",
        section("Success criteria", spec.success_criteria),
        "",
        section("Stop criteria", spec.stop_criteria),
        "",
        section("Requested topics", spec.requested_topics),
        "",
        section("Ambiguity flags", spec.ambiguity_flags),
        "",
        section("Clarification questions", spec.clarification_questions),
        "",
        section("Handoff conditions", spec.handoff_conditions),
        "",
        section("Boundary topics", spec.boundary_topics),
        "",
        section("Assumptions", spec.assumptions),
    ]
    return "\n".join(parts)


def render_handoff_markdown(note: HandoffNote) -> str:
    sections = [
        f"# Handoff / Clarification Outcome ({note.outcome})",
        "",
        "## Summary",
        "",
        note.summary,
        "",
        "## Missing information or blockers",
        "",
    ]
    if note.missing_information:
        sections.extend(f"- {item}" for item in note.missing_information)
    else:
        sections.append("- None")
    sections.extend(["", "## Next actions", ""])
    if note.next_actions:
        sections.extend(f"- {item}" for item in note.next_actions)
    else:
        sections.append("- None")
    sections.extend(["", "## Boundary topics", ""])
    if note.boundary_topics:
        sections.extend(f"- {item}" for item in note.boundary_topics)
    else:
        sections.append("- None")
    return "\n".join(sections)


def emit_task_spec(spec: TaskSpec, out_dir: str | Path) -> Path:
    target = ensure_dir(out_dir)
    write_json(target / "task_spec.json", spec)
    write_text(target / "task_spec.md", render_task_spec_markdown(spec))
    return target


def emit_run_artifacts(result: RunResult, out_dir: str | Path) -> Path:
    target = ensure_dir(out_dir)
    write_json(target / "plan.json", result.plan)
    write_jsonl(target / "trace.jsonl", result.trace)
    write_jsonl(target / "state_snapshots.jsonl", result.state_snapshots)
    write_jsonl(target / "memory_log.jsonl", result.memory_log)
    write_jsonl(target / "tool_observations.jsonl", result.tool_observations)
    write_jsonl(target / "verification.jsonl", result.verification_results)
    write_json(target / "stop_decision.json", result.stop_decision)
    write_json(target / "run_summary.json", result.run_summary)
    if result.final_review_md:
        write_text(target / "final_review.md", result.final_review_md)
    if result.handoff_note:
        write_text(target / "handoff_note.md", render_handoff_markdown(result.handoff_note))
    return target


def emit_comparison_artifacts(
    out_dir: str | Path,
    comparison_matrix_md: str,
    fit_recommendation_md: str,
    failure_diagnosis_md: str,
    boundary_note_md: str | None = None,
) -> Path:
    target = ensure_dir(out_dir)
    write_text(target / "comparison_matrix.md", comparison_matrix_md)
    write_text(target / "fit_recommendation.md", fit_recommendation_md)
    write_text(target / "failure_diagnosis.md", failure_diagnosis_md)
    if boundary_note_md is not None:
        write_text(target / "boundary_note.md", boundary_note_md)
    return target
