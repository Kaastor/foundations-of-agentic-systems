from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .schemas import StateSnapshot, TraceEvent, VerificationResult


@dataclass
class RunState:
    task_spec: Any
    variant: str
    step: int = 0
    active_context: dict[str, Any] = field(default_factory=dict)
    external_state: dict[str, Any] = field(default_factory=dict)
    unresolved_issues: list[str] = field(default_factory=list)
    trace: list[TraceEvent] = field(default_factory=list)
    state_snapshots: list[StateSnapshot] = field(default_factory=list)
    verification_results: list[VerificationResult] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.active_context = {
            "focus_topics": list(self.task_spec.requested_topics),
            "current_action": None,
            "current_plan_step": None,
            "recent_observation_refs": [],
            "recent_memory_refs": [],
        }
        self.external_state = {
            "search_queries": [],
            "selected_papers": [],
            "read_papers": [],
            "written_notes": [],
            "final_citations": [],
            "review_sources": [],
            "review_covered_topics": [],
            "reflection_actions": [],
            "comparison_done": False,
            "recommendation_made": False,
            "clarification_emitted": False,
            "boundary_note_emitted": False,
            "used_memory_entries": [],
            "used_stale_memory": False,
            "draft_review": None,
        }

    def next_step(self) -> int:
        self.step += 1
        return self.step

    def record_trace(
        self,
        phase: str,
        event_type: str,
        message: str,
        action_name: str | None = None,
        evidence_refs: list[str] | None = None,
        data: dict[str, Any] | None = None,
    ) -> None:
        self.trace.append(
            TraceEvent(
                step=self.step,
                phase=phase,
                event_type=event_type,
                message=message,
                action_name=action_name,
                evidence_refs=list(evidence_refs or []),
                data=dict(data or {}),
            )
        )

    def record_verification(self, result: VerificationResult) -> None:
        self.verification_results.append(result)
        self.unresolved_issues = list(result.blocking_issues)

    def push_observation_refs(self, refs: list[str], window: int) -> None:
        merged = self.active_context["recent_observation_refs"] + refs
        self.active_context["recent_observation_refs"] = merged[-window:]

    def push_memory_refs(self, refs: list[str], window: int) -> None:
        merged = self.active_context["recent_memory_refs"] + refs
        self.active_context["recent_memory_refs"] = merged[-window:]

    def snapshot(self, memory_summary: dict[str, Any], world_outcomes: dict[str, Any] | None = None) -> None:
        self.state_snapshots.append(
            StateSnapshot(
                step=self.step,
                active_context=dict(self.active_context),
                external_state={
                    "search_queries": list(self.external_state["search_queries"]),
                    "selected_papers": list(self.external_state["selected_papers"]),
                    "read_papers": [paper["citation_id"] for paper in self.external_state["read_papers"]],
                    "written_notes": list(self.external_state["written_notes"]),
                    "final_citations": list(self.external_state["final_citations"]),
                    "review_sources": list(self.external_state["review_sources"]),
                    "review_covered_topics": list(self.external_state["review_covered_topics"]),
                    "reflection_actions": list(self.external_state["reflection_actions"]),
                    "clarification_emitted": self.external_state["clarification_emitted"],
                    "boundary_note_emitted": self.external_state["boundary_note_emitted"],
                },
                memory_summary=memory_summary,
                world_outcomes=dict(world_outcomes or {}),
                unresolved_issues=list(self.unresolved_issues),
            )
        )
