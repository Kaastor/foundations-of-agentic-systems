from __future__ import annotations

from .schemas import Plan, PlanStep, VerificationResult

TOPIC_QUERIES: dict[str, str] = {
    "planning": "planning decomposition lightweight planning replan",
    "memory": "memory notes forgetting recall retention",
    "grounding": "grounding evidence citations evidence linked verifiable claims claim checking",
    "tools": "tool interface local research tools evidence linking",
    "reflection": "reflection verification feedback evidence backed verification",
    "stopping": "clarification handoff bounded autonomy stop criteria",
    "state": "state context execution trace outcomes",
    "goals": "goal task specification success criteria stop criteria",
    "model_baselines": "model-only scripted baseline direct generation",
    "architecture_comparison": "architecture comparison task fit tradeoff variants",
    "agent_loop": "control loop observe think act trace",
}


def build_initial_plan(task_spec, variant: str) -> Plan:
    labels = []
    if task_spec.ambiguity_flags or task_spec.boundary_topics:
        labels.append(("assess_scope", "think", "Check ambiguity and scope boundaries before acting."))
    if variant in {"tool_rich_memoryless", "memory_rich_tool_poor", "capstone_agent"}:
        labels.append(("prepare", "think", "Retrieve memory or search context before reading papers."))
    else:
        labels.append(("prepare", "think", "Prepare the fixed baseline flow."))
    labels.extend(
        [
            ("collect_evidence", "act", "Collect evidence from the local corpus."),
            ("verify_coverage", "verify", "Check topic coverage before drafting."),
            ("synthesize", "act", "Draft the review from available evidence."),
            ("final_verify", "verify", "Check final success criteria before stopping."),
            ("stop_or_handoff", "stop", "Stop successfully or emit a bounded handoff outcome."),
        ]
    )
    return Plan(
        variant=variant,
        steps=[PlanStep(step_id=f"{index+1:02d}", label=label, action=action, rationale=rationale) for index, (label, action, rationale) in enumerate(labels)],
    )


def mark_plan_step(plan: Plan, label: str, status: str) -> None:
    for step in plan.steps:
        if step.label == label:
            step.status = status
            return


def select_papers(results: list[dict], requested_topics: list[str], budget: int, strategy: str) -> list[dict]:
    unique_results = []
    seen = set()
    for result in results:
        if result["citation_id"] not in seen:
            seen.add(result["citation_id"])
            unique_results.append(result)
    if strategy == "greedy":
        return unique_results[:budget]
    selected: list[dict] = []
    covered: set[str] = set()
    remaining = unique_results.copy()
    while remaining and len(selected) < budget:
        remaining.sort(
            key=lambda item: (
                -len(set(item.get("topic_tags", [])) & set(requested_topics) - covered),
                -item.get("score", 0),
                item["citation_id"],
            )
        )
        choice = remaining.pop(0)
        selected.append(choice)
        covered |= set(choice.get("topic_tags", [])) & set(requested_topics)
    return selected


def topic_query(topic: str) -> str:
    return TOPIC_QUERIES.get(topic, topic.replace("_", " "))


def needs_replan(result: VerificationResult) -> bool:
    return any(issue.startswith("planning: missing topic coverage") for issue in result.blocking_issues)


def missing_topics_from_verification(result: VerificationResult) -> list[str]:
    topics: list[str] = []
    for issue in result.blocking_issues:
        if issue.startswith("planning: missing topic coverage for "):
            tail = issue.removeprefix("planning: missing topic coverage for ")
            topics.extend(part.strip() for part in tail.split(",") if part.strip())
    return list(dict.fromkeys(topics))


def replan(plan: Plan, missing_topics: list[str]) -> Plan:
    plan.replans += 1
    plan.steps.insert(
        -2,
        PlanStep(
            step_id=f"r{plan.replans:02d}",
            label="replan_search",
            action="act",
            rationale=f"Search again for missing topics: {', '.join(missing_topics)}.",
            status="pending",
        ),
    )
    return plan
