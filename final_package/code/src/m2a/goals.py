from __future__ import annotations

import re
from pathlib import Path

from .schemas import TaskSpec

TOPIC_ALIASES: dict[str, tuple[str, ...]] = {
    "agent_loop": ("control loop", "agent loop", "observe-think-act", "loop"),
    "goals": ("goal", "task specification", "success criteria", "stop criteria"),
    "state": ("state", "context", "trace", "execution trace"),
    "memory": ("memory", "notes", "recall", "forget"),
    "tools": ("tool", "tool interface", "tool use", "interface"),
    "grounding": ("grounding", "evidence-backed", "evidence linked", "citation", "verifiable claim", "claim checking"),
    "planning": ("planning", "decomposition", "replan", "lightweight planning"),
    "reflection": ("reflection", "verification", "self-critique", "feedback"),
    "stopping": ("stop criteria", "handoff", "clarification", "bounded autonomy", "stopping"),
    "model_baselines": ("model-only", "bare model", "scripted baseline", "baseline"),
    "architecture_comparison": ("compare architectures", "architecture comparison", "tradeoff", "variant"),
}

BOUNDARY_KEYWORDS: dict[str, tuple[str, ...]] = {
    "rl_control": ("reinforcement learning", "rl", "policy learning"),
    "ir_internals": ("bm25", "vector ranking", "index internals", "retrieval ranking"),
    "live_retrieval": ("live web", "web retrieval", "external api", "internet"),
    "symbolic_planning": ("pddl", "symbolic planning", "planner formalism"),
    "operations": ("deployment", "observability", "incident response", "production architecture"),
    "frameworks": ("langchain", "orchestration product", "vendor sdk"),
}

AMBIGUOUS_CUES: tuple[str, ...] = (
    "important",
    "best",
    "latest",
    "recent",
    "what matters",
    "top papers",
)


def _slugify(text: str) -> str:
    words = re.findall(r"[a-z0-9]+", text.lower())
    return "-".join(words[:8]) or "request"


def read_request_input(value_or_path: str) -> tuple[str, str]:
    possible_path = Path(value_or_path)
    if possible_path.exists():
        return possible_path.read_text(encoding="utf-8"), possible_path.stem
    return value_or_path, _slugify(value_or_path)


def _normalize(text: str) -> str:
    return " ".join(text.split())


def _contains_alias(text: str, alias: str) -> bool:
    alias = alias.lower()
    if " " in alias or "-" in alias:
        return alias in text
    return re.search(rf"\b{re.escape(alias)}\b", text) is not None


def _parse_paper_budget(text: str) -> tuple[int, int, list[str]]:
    lowered = text.lower()
    assumptions: list[str] = []
    range_match = re.search(r"(\d+)\s*(?:to|-)\s*(\d+)\s+local\s+papers", lowered)
    if not range_match:
        range_match = re.search(r"(\d+)\s*(?:to|-)\s*(\d+)\s+papers", lowered)
    if range_match:
        return int(range_match.group(1)), int(range_match.group(2)), assumptions
    exact_match = re.search(r"cite\s+(\d+)\s+local\s+papers", lowered) or re.search(r"use\s+(\d+)\s+local\s+papers", lowered)
    if exact_match:
        count = int(exact_match.group(1))
        return count, count, assumptions
    at_most = re.search(r"(?:at most|up to|no more than)\s+(\d+)\s+papers", lowered)
    if at_most:
        maximum = int(at_most.group(1))
        return min(2, maximum), maximum, assumptions
    assumptions.append("No explicit paper budget was given; defaulted to 3 to 5 local papers.")
    return 3, 5, assumptions


def _detect_topics(text: str) -> list[str]:
    lowered = text.lower()
    topics: list[str] = []
    for topic, aliases in TOPIC_ALIASES.items():
        if any(_contains_alias(lowered, alias) for alias in aliases):
            topics.append(topic)
    return topics


def _detect_boundary_topics(text: str) -> list[str]:
    lowered = text.lower()
    hits: list[str] = []
    for boundary, aliases in BOUNDARY_KEYWORDS.items():
        if any(_contains_alias(lowered, alias) for alias in aliases):
            hits.append(boundary)
    return hits


def _detect_ambiguity(text: str, topics: list[str]) -> tuple[list[str], list[str]]:
    lowered = text.lower()
    flags: list[str] = []
    questions: list[str] = []
    if not topics:
        flags.append("No explicit topical focus was provided.")
        questions.append("Which agent architecture concepts should the review cover?")
    for cue in AMBIGUOUS_CUES:
        if cue in lowered:
            flags.append(f"The request uses the ambiguous phrase '{cue}'.")
    if "agents" in lowered and "literature review" not in lowered and not topics:
        flags.append("The domain is broad enough that the local corpus may not match the user's intent.")
    if flags and not questions:
        questions.append("What exact scope should the review cover inside the local corpus?")
    return list(dict.fromkeys(flags)), questions


def build_task_spec(request_text: str, request_id: str | None = None) -> TaskSpec:
    normalized = _normalize(request_text)
    topics = _detect_topics(normalized)
    ambiguity_flags, clarification_questions = _detect_ambiguity(normalized, topics)
    boundary_topics = _detect_boundary_topics(normalized)
    budget_min, budget_max, assumptions = _parse_paper_budget(normalized)
    comparison_mode = any(marker in normalized.lower() for marker in ("compare", "tradeoff", "versus", "vs"))
    recommendation_required = any(marker in normalized.lower() for marker in ("recommend", "better architecture", "should"))
    goals = ["Produce a bounded literature review using only the shipped local corpus."]
    goals.extend(f"Explain {topic.replace('_', ' ')} with explicit evidence." for topic in topics)
    if comparison_mode:
        goals.append("Compare the requested alternatives rather than listing papers independently.")
    if recommendation_required:
        goals.append("Defend one bounded architecture recommendation with evidence.")
    constraints = [
        "Use local corpus papers only; no live retrieval or external APIs.",
        "Keep the run deterministic and inspectable.",
        f"Use between {budget_min} and {budget_max} papers unless a valid handoff occurs.",
    ]
    subgoals = [
        "Formalize the review request into explicit goals, constraints, and stop rules.",
        "Collect evidence from the local paper corpus.",
        "Synthesize a citation-backed review or emit a bounded handoff outcome.",
    ]
    if comparison_mode:
        subgoals.append("Surface the tradeoff between the compared architecture choices.")
    success_criteria = [
        "Every requested topic is covered by evidence from at least one local paper.",
        "The final review includes citations assembled from the local corpus.",
    ]
    if comparison_mode:
        success_criteria.append("The final review contains a direct comparison of the requested alternatives.")
    if recommendation_required:
        success_criteria.append("The final review contains an evidence-backed recommendation.")
    stop_criteria = [
        "Stop successfully only when all success criteria are satisfied.",
        "Emit a clarification or handoff outcome when ambiguity or scope boundaries block a safe review.",
        "If blocking issues remain after bounded replanning, stop with an explicit bounded failure or handoff.",
    ]
    handoff_conditions = [
        "Ambiguity remains unresolved after task formalization.",
        "The request depends on out-of-scope topics such as RL, IR internals, live retrieval, symbolic planning, or operations.",
        "The local corpus cannot support the requested evidence within the paper budget.",
    ]
    if not assumptions:
        assumptions.append("The intended audience is a beginner seeking structural literacy rather than domain specialization.")
    if not topics and not boundary_topics:
        assumptions.append("Because no topics were explicit, the system will prefer clarification over guessing.")
    return TaskSpec(
        request_id=request_id or _slugify(normalized),
        raw_request=request_text.strip(),
        normalized_request=normalized,
        goals=goals,
        constraints=constraints,
        subgoals=subgoals,
        success_criteria=success_criteria,
        stop_criteria=stop_criteria,
        ambiguity_flags=ambiguity_flags,
        clarification_questions=clarification_questions,
        handoff_conditions=handoff_conditions,
        requested_topics=topics,
        boundary_topics=boundary_topics,
        assumptions=assumptions,
        paper_budget_min=budget_min,
        paper_budget_max=budget_max,
        comparison_mode=comparison_mode,
        recommendation_required=recommendation_required,
        max_steps=20,
    ).validate()
