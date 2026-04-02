from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(slots=True)
class TaskSpec:
    request_id: str
    raw_request: str
    normalized_request: str
    goals: list[str]
    constraints: list[str]
    subgoals: list[str]
    success_criteria: list[str]
    stop_criteria: list[str]
    ambiguity_flags: list[str]
    clarification_questions: list[str]
    handoff_conditions: list[str]
    requested_topics: list[str]
    boundary_topics: list[str]
    assumptions: list[str]
    paper_budget_min: int
    paper_budget_max: int
    comparison_mode: bool
    recommendation_required: bool
    max_steps: int = 8

    def validate(self) -> "TaskSpec":
        if not self.request_id:
            raise ValueError("request_id must be non-empty")
        if not self.normalized_request:
            raise ValueError("normalized_request must be non-empty")
        if self.paper_budget_min <= 0 or self.paper_budget_max <= 0:
            raise ValueError("paper budgets must be positive")
        if self.paper_budget_min > self.paper_budget_max:
            raise ValueError("paper_budget_min cannot exceed paper_budget_max")
        if self.max_steps <= 0:
            raise ValueError("max_steps must be positive")
        self.requested_topics = list(dict.fromkeys(self.requested_topics))
        self.boundary_topics = list(dict.fromkeys(self.boundary_topics))
        return self

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "TaskSpec":
        return cls(**data).validate()

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class PlanStep:
    step_id: str
    label: str
    action: str
    rationale: str
    status: str = "pending"


@dataclass(slots=True)
class Plan:
    variant: str
    steps: list[PlanStep]
    replans: int = 0

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class ActionProposal:
    action_name: str
    payload: dict[str, Any]
    rationale: str
    evidence_refs: list[str] = field(default_factory=list)


@dataclass(slots=True)
class TraceEvent:
    step: int
    phase: str
    event_type: str
    message: str
    action_name: str | None = None
    evidence_refs: list[str] = field(default_factory=list)
    data: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class StateSnapshot:
    step: int
    active_context: dict[str, Any]
    external_state: dict[str, Any]
    memory_summary: dict[str, Any]
    world_outcomes: dict[str, Any]
    unresolved_issues: list[str]


@dataclass(slots=True)
class MemoryItem:
    entry_id: str
    memory_type: str
    content: str
    source_refs: list[str]
    tags: list[str]
    created_step: int = 0
    stale: bool = False

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "MemoryItem":
        return cls(**data)


@dataclass(slots=True)
class MemoryLogEvent:
    step: int
    event_type: str
    entry_id: str
    memory_type: str
    content: str
    source_refs: list[str]
    tags: list[str]
    policy_reason: str
    stale: bool = False
    policy: dict[str, Any] | None = None


@dataclass(slots=True)
class ToolObservation:
    step: int
    tool_name: str
    success: bool
    input: dict[str, Any]
    output: dict[str, Any]
    summary: str
    source_refs: list[str] = field(default_factory=list)
    side_effects: list[str] = field(default_factory=list)


@dataclass(slots=True)
class VerificationResult:
    step: int
    stage: str
    satisfied: bool
    checks: dict[str, bool]
    blocking_issues: list[str]
    non_blocking_issues: list[str]
    evidence_refs: list[str] = field(default_factory=list)


@dataclass(slots=True)
class StopDecision:
    step: int
    outcome: str
    rationale: str
    satisfied_success_criteria: list[str]
    remaining_blockers: list[str]
    handoff_required: bool
    boundary_topics: list[str] = field(default_factory=list)


@dataclass(slots=True)
class HandoffNote:
    outcome: str
    summary: str
    missing_information: list[str]
    next_actions: list[str]
    boundary_topics: list[str] = field(default_factory=list)


@dataclass(slots=True)
class RunResult:
    variant: str
    plan: Plan
    trace: list[TraceEvent]
    state_snapshots: list[StateSnapshot]
    memory_log: list[MemoryLogEvent]
    tool_observations: list[ToolObservation]
    stop_decision: StopDecision
    verification_results: list[VerificationResult]
    run_summary: dict[str, Any]
    final_review_md: str | None = None
    handoff_note: HandoffNote | None = None


@dataclass(slots=True)
class ArchitectureAssessment:
    variant: str
    outcome: str
    success: bool
    tool_calls: int
    papers_read: int
    citations_used: int
    memory_events: int
    reflection_events: int
    used_tools: list[str]
    diagnoses: list[str]
    blocking_issues: list[str]
    notes: str
