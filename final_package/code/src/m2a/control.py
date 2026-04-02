from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .baselines import run_model_only, run_scripted_pipeline
from .feedback import diagnose_failure, evaluate_progress, reflection_actions
from .memory import DEFAULT_MEMORY_PATH, MemoryPolicy, MemoryStore, load_seed_memory
from .planning import build_initial_plan, mark_plan_step, missing_topics_from_verification, needs_replan, replan, select_papers, topic_query
from .schemas import ActionProposal, HandoffNote, RunResult, StopDecision
from .state import RunState
from .synthesis import draft_review
from .tools import ToolBox

REPO_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True, slots=True)
class VariantProfile:
    name: str
    can_search: bool
    can_read: bool
    can_write_notes: bool
    uses_memory: bool
    allow_stale_memory: bool
    planning_strategy: str
    handle_ambiguity: bool
    reflection_enabled: bool
    context_window: int
    max_steps: int


VARIANT_PROFILES = {
    "tool_rich_memoryless": VariantProfile(
        name="tool_rich_memoryless",
        can_search=True,
        can_read=True,
        can_write_notes=False,
        uses_memory=False,
        allow_stale_memory=False,
        planning_strategy="coverage",
        handle_ambiguity=False,
        reflection_enabled=True,
        context_window=2,
        max_steps=16,
    ),
    "memory_rich_tool_poor": VariantProfile(
        name="memory_rich_tool_poor",
        can_search=False,
        can_read=True,
        can_write_notes=True,
        uses_memory=True,
        allow_stale_memory=True,
        planning_strategy="memory_first",
        handle_ambiguity=True,
        reflection_enabled=True,
        context_window=3,
        max_steps=16,
    ),
    "capstone_agent": VariantProfile(
        name="capstone_agent",
        can_search=True,
        can_read=True,
        can_write_notes=True,
        uses_memory=True,
        allow_stale_memory=False,
        planning_strategy="coverage",
        handle_ambiguity=True,
        reflection_enabled=True,
        context_window=4,
        max_steps=20,
    ),
}

VALID_VARIANTS = ("model_only", "scripted_pipeline", "tool_rich_memoryless", "memory_rich_tool_poor", "capstone_agent")


def _memory_policy_for(profile: VariantProfile) -> MemoryPolicy:
    if profile.name == "memory_rich_tool_poor":
        return MemoryPolicy(name="memory_rich_tool_poor", max_entries=12, retrieval_limit=4, stale_after_steps=999, allow_writes=True, allow_stale_recall=True)
    if profile.name == "capstone_agent":
        return MemoryPolicy(name="capstone_agent", max_entries=12, retrieval_limit=4, stale_after_steps=5, allow_writes=True, allow_stale_recall=False)
    return MemoryPolicy(name=profile.name, max_entries=2, retrieval_limit=2, stale_after_steps=0, allow_writes=False, allow_stale_recall=False)


def _make_toolbox(run_dir: str | Path) -> ToolBox:
    return ToolBox(note_dir=Path(run_dir) / "notes")


def _propose_next_action(state: RunState, profile: VariantProfile, plan, memory_store: MemoryStore) -> ActionProposal:
    if state.task_spec.boundary_topics and profile.handle_ambiguity and not state.external_state["boundary_note_emitted"]:
        return ActionProposal("handoff_boundary", {}, "The request crosses an explicit repository boundary.")
    if state.task_spec.ambiguity_flags and profile.handle_ambiguity and not state.external_state["clarification_emitted"]:
        return ActionProposal("clarify", {"questions": state.task_spec.clarification_questions}, "The request needs clarification before bounded action.")
    if profile.uses_memory and not state.external_state["used_memory_entries"]:
        return ActionProposal("retrieve_memory", {"query_terms": state.task_spec.requested_topics}, "Consult memory before collecting or drafting evidence.")
    pending_missing = [action.split(":", 1)[1] for action in state.external_state["reflection_actions"] if action.startswith("search:")]
    if pending_missing and profile.can_search:
        topic = pending_missing[0]
        return ActionProposal("search", {"query": topic_query(topic), "reason_topic": topic}, "A verified topic gap triggered replanning.")
    if not state.external_state["selected_papers"]:
        if profile.can_search:
            query = " ".join(topic_query(topic) for topic in state.task_spec.requested_topics) or state.task_spec.normalized_request
            return ActionProposal("search", {"query": query, "reason_topic": None}, "Collect candidate papers from the local corpus.")
        if profile.uses_memory:
            memory_refs = []
            for item in memory_store.retrieve(state.task_spec.requested_topics, state.step):
                memory_refs.extend(item.source_refs)
            memory_refs = list(dict.fromkeys(ref for ref in memory_refs if ref))
            return ActionProposal("seed_from_memory", {"citation_ids": memory_refs}, "Without search, use memory-linked citations as the candidate set.")
    selected_ids = state.external_state["selected_papers"]
    read_ids = {paper["citation_id"] for paper in state.external_state["read_papers"]}
    unread = [citation_id for citation_id in selected_ids if citation_id not in read_ids]
    if unread and len(state.external_state["read_papers"]) < state.task_spec.paper_budget_max:
        return ActionProposal("read", {"citation_id": unread[0]}, "Read the next selected paper.")
    if profile.can_write_notes:
        read_without_notes = [paper for paper in state.external_state["read_papers"] if paper["citation_id"] not in {note["citation_id"] for note in state.external_state.get("note_index", [])}]
        if read_without_notes:
            paper = read_without_notes[0]
            return ActionProposal("write_note", {"paper": paper}, "Persist the latest paper as evidence-linked memory.")
    if len(state.external_state["read_papers"]) >= state.task_spec.paper_budget_min and not state.external_state.get("intermediate_verified"):
        return ActionProposal("verify", {"stage": "intermediate"}, "Check coverage before drafting.")
    if state.external_state["draft_review"] is None and state.external_state.get("intermediate_verified", False):
        return ActionProposal("synthesize", {}, "Draft the review from the available evidence.")
    if state.external_state["draft_review"] is None and len(state.external_state["read_papers"]) >= state.task_spec.paper_budget_min:
        return ActionProposal("synthesize", {}, "Draft the review from the bounded evidence set.")
    if state.external_state["draft_review"] is not None and not state.external_state["final_citations"]:
        return ActionProposal("assemble_citations", {}, "Assemble citations before the final stop decision.")
    if state.external_state["draft_review"] is not None:
        return ActionProposal("stop", {}, "A draft exists; run final verification and stop or hand off.")
    return ActionProposal("stop", {}, "No further bounded action is available.")


def _make_handoff(task_spec, outcome: str, blockers: list[str], boundary: bool = False) -> HandoffNote:
    if outcome == "clarification_needed":
        next_actions = ["Answer the clarification questions and rerun spec-review."]
        missing = list(task_spec.clarification_questions) or list(blockers)
    elif boundary:
        next_actions = ["Move this request to a specialized track covering the deferred topics."]
        missing = list(blockers) or ["The request depends on explicitly deferred topics."]
    else:
        next_actions = ["Use a variant with the missing capability or narrow the task scope."]
        missing = list(blockers)
    return HandoffNote(
        outcome=outcome,
        summary="The run stopped with a bounded non-success outcome because the current architecture could not safely satisfy the task.",
        missing_information=missing,
        next_actions=next_actions,
        boundary_topics=list(task_spec.boundary_topics),
    )


def _stop_decision(state: RunState, verification, outcome: str, rationale: str) -> StopDecision:
    success_criteria = list(state.task_spec.success_criteria) if verification.satisfied else []
    return StopDecision(
        step=state.step,
        outcome=outcome,
        rationale=rationale,
        satisfied_success_criteria=success_criteria,
        remaining_blockers=list(verification.blocking_issues),
        handoff_required=outcome != "success",
        boundary_topics=list(state.task_spec.boundary_topics),
    )


def _finalize_result(profile: VariantProfile, state: RunState, plan, memory_store: MemoryStore, tool_observations, final_review_md=None, handoff_note=None) -> RunResult:
    verification = state.verification_results[-1]
    if verification.satisfied and handoff_note is None:
        stop = _stop_decision(state, verification, "success", "All final success checks passed.")
    else:
        outcome = handoff_note.outcome if handoff_note else "bounded_failure"
        stop = _stop_decision(state, verification, outcome, "The latest verification still contains blocking issues.")
    result = RunResult(
        variant=profile.name,
        plan=plan,
        trace=state.trace,
        state_snapshots=state.state_snapshots,
        memory_log=list(memory_store.events),
        tool_observations=list(tool_observations),
        stop_decision=stop,
        verification_results=state.verification_results,
        run_summary={
            "read_papers": [paper["citation_id"] for paper in state.external_state["read_papers"]],
            "final_citations": list(state.external_state["final_citations"]),
            "reflection_actions": list(state.external_state["reflection_actions"]),
            "used_memory_entries": list(state.external_state["used_memory_entries"]),
            "used_stale_memory": state.external_state["used_stale_memory"],
            "diagnoses": diagnose_failure(
                RunResult(
                    variant=profile.name,
                    plan=plan,
                    trace=[],
                    state_snapshots=[],
                    memory_log=[],
                    tool_observations=[],
                    stop_decision=stop,
                    verification_results=state.verification_results,
                    run_summary={},
                ),
                verification,
            ),
        },
        final_review_md=final_review_md if handoff_note is None else None,
        handoff_note=handoff_note,
    )
    return result


def _run_profile(task_spec, profile: VariantProfile, run_dir: str | Path) -> RunResult:
    toolbox = _make_toolbox(run_dir)
    plan = build_initial_plan(task_spec, profile.name)
    state = RunState(task_spec, profile.name)
    tool_observations = []
    memory_store = MemoryStore(_memory_policy_for(profile), load_seed_memory(DEFAULT_MEMORY_PATH) if profile.uses_memory else [])
    state.external_state["note_index"] = []

    state.next_step()
    state.record_trace("observe", "task_received", "Received structured task spec.")
    state.snapshot(memory_store.diagnostics(), {"drafted": False})

    step_limit = min(profile.max_steps, task_spec.max_steps)
    while state.step < step_limit:
        proposal = _propose_next_action(state, profile, plan, memory_store)
        state.next_step()
        state.active_context["current_action"] = proposal.action_name
        state.record_trace("think", "action_proposed", proposal.rationale, action_name=proposal.action_name, evidence_refs=proposal.evidence_refs, data=proposal.payload)

        if proposal.action_name == "handoff_boundary":
            mark_plan_step(plan, "assess_scope", "done")
            state.external_state["boundary_note_emitted"] = True
            verification = evaluate_progress(task_spec, state, stage="final")
            state.record_verification(verification)
            state.record_trace("stop", "boundary_note", "Stopped because the request crossed an explicit boundary.", action_name="handoff_boundary", data={"blocking_issues": verification.blocking_issues})
            state.snapshot(memory_store.diagnostics(), {"boundary_note": True})
            handoff = _make_handoff(task_spec, "handoff", verification.blocking_issues, boundary=True)
            return _finalize_result(profile, state, plan, memory_store, tool_observations, None, handoff)

        if proposal.action_name == "clarify":
            mark_plan_step(plan, "assess_scope", "done")
            state.external_state["clarification_emitted"] = True
            verification = evaluate_progress(task_spec, state, stage="final")
            state.record_verification(verification)
            state.record_trace("stop", "clarification_needed", "Stopped because the request is too ambiguous for bounded execution.", action_name="clarify", data={"questions": task_spec.clarification_questions})
            state.snapshot(memory_store.diagnostics(), {"clarification": True})
            handoff = _make_handoff(task_spec, "clarification_needed", verification.blocking_issues)
            return _finalize_result(profile, state, plan, memory_store, tool_observations, None, handoff)

        if proposal.action_name == "retrieve_memory":
            mark_plan_step(plan, "prepare", "done")
            items = memory_store.retrieve(proposal.payload["query_terms"], state.step)
            state.external_state["used_memory_entries"] = [item.entry_id for item in items]
            state.push_memory_refs([item.entry_id for item in items], profile.context_window)
            state.record_trace("update", "memory_retrieved", f"Retrieved {len(items)} memory item(s).", action_name="retrieve_memory", evidence_refs=[item.entry_id for item in items])
            state.snapshot(memory_store.diagnostics(), {"memory_hits": [item.entry_id for item in items]})
            continue

        if proposal.action_name == "seed_from_memory":
            mark_plan_step(plan, "prepare", "done")
            state.external_state["selected_papers"] = proposal.payload["citation_ids"][: task_spec.paper_budget_max]
            state.record_trace("update", "candidate_set_seeded", "Seeded the candidate set from memory-linked citations.", action_name="seed_from_memory", evidence_refs=state.external_state["selected_papers"])
            state.snapshot(memory_store.diagnostics(), {"selected": state.external_state["selected_papers"]})
            continue

        if proposal.action_name == "search":
            mark_plan_step(plan, "collect_evidence", "done")
            query = proposal.payload["query"]
            search_obs = toolbox.search_corpus(query, max(task_spec.paper_budget_max + 1, 4), state.step)
            tool_observations.append(search_obs)
            state.external_state["search_queries"].append(query)
            state.record_trace("act", "tool_call", search_obs.summary, action_name="search_corpus", evidence_refs=search_obs.source_refs, data={"query": query})
            selection_strategy = "coverage" if profile.planning_strategy == "coverage" else "greedy"
            selected = select_papers(search_obs.output["results"], task_spec.requested_topics, task_spec.paper_budget_max, strategy=selection_strategy)
            for item in selected:
                if item["citation_id"] not in state.external_state["selected_papers"]:
                    state.external_state["selected_papers"].append(item["citation_id"])
            reason_topic = proposal.payload.get("reason_topic")
            if reason_topic:
                state.external_state["reflection_actions"] = [action for action in state.external_state["reflection_actions"] if action != f"search:{reason_topic}"]
            state.push_observation_refs(search_obs.source_refs, profile.context_window)
            state.snapshot(memory_store.diagnostics(), {"selected": state.external_state["selected_papers"]})
            continue

        if proposal.action_name == "read":
            citation_id = proposal.payload["citation_id"]
            read_obs = toolbox.read_paper(citation_id, state.step)
            tool_observations.append(read_obs)
            paper = read_obs.output
            state.external_state["read_papers"].append(paper)
            state.record_trace("act", "tool_call", read_obs.summary, action_name="read_paper", evidence_refs=[citation_id])
            state.push_observation_refs([citation_id], profile.context_window)
            state.snapshot(memory_store.diagnostics(), {"last_read": citation_id})
            continue

        if proposal.action_name == "write_note":
            paper = proposal.payload["paper"]
            note_title = f"{paper['citation_id']} note"
            note_body = paper["findings"][0]
            note_obs = toolbox.write_note(note_title, note_body, [paper["citation_id"]], state.step)
            tool_observations.append(note_obs)
            state.external_state["written_notes"].append(note_obs.output["note_path"])
            state.external_state["note_index"].append({"citation_id": paper["citation_id"], "note_path": note_obs.output["note_path"]})
            state.record_trace("act", "tool_call", note_obs.summary, action_name="write_note", evidence_refs=[paper["citation_id"]])
            memory_store.write(
                memory_type="note",
                content=f"{paper['title']}: {paper['findings'][0]}",
                source_refs=[paper["citation_id"]],
                tags=paper["topic_tags"],
                step=state.step,
            )
            state.snapshot(memory_store.diagnostics(), {"last_note": note_obs.output["note_path"]})
            continue

        if proposal.action_name == "verify":
            mark_plan_step(plan, "verify_coverage", "done")
            verification = evaluate_progress(task_spec, state, stage=proposal.payload["stage"])
            state.record_verification(verification)
            state.record_trace("verify", "verification_result", "Checked progress against blocking criteria.", action_name="verify", evidence_refs=verification.evidence_refs, data={"blocking_issues": verification.blocking_issues})
            state.external_state["intermediate_verified"] = verification.satisfied
            if profile.reflection_enabled and needs_replan(verification) and profile.can_search:
                missing_topics = missing_topics_from_verification(verification)
                replan(plan, missing_topics)
                state.external_state["reflection_actions"].extend(reflection_actions(verification))
                state.record_trace("update", "replan", f"Replanned for missing topics: {', '.join(missing_topics)}.", action_name="replan", evidence_refs=verification.evidence_refs)
            state.snapshot(memory_store.diagnostics(), {"verified": verification.satisfied})
            continue

        if proposal.action_name == "synthesize":
            mark_plan_step(plan, "synthesize", "done")
            memory_items = []
            if profile.uses_memory:
                memory_items = memory_store.retrieve(task_spec.requested_topics, state.step)
                state.external_state["used_memory_entries"] = [item.entry_id for item in memory_items]
                state.external_state["used_stale_memory"] = any(item.stale for item in memory_items)
            if profile.uses_memory and profile.can_write_notes:
                source_ids = []
                for item in memory_items:
                    source_ids.extend(item.source_refs)
                source_ids = list(dict.fromkeys(source_ids))
                candidate_papers = {paper["citation_id"]: paper for paper in state.external_state["read_papers"]}
                papers = [candidate_papers[citation_id] for citation_id in source_ids if citation_id in candidate_papers]
                if not papers:
                    papers = state.external_state["read_papers"]
            else:
                recent_ids = set(state.active_context["recent_observation_refs"])
                papers = [paper for paper in state.external_state["read_papers"] if paper["citation_id"] in recent_ids]
                if not papers:
                    papers = state.external_state["read_papers"][-profile.context_window :]
            review_md, metadata = draft_review(task_spec, profile.name, papers, memory_items if profile.uses_memory else None)
            state.external_state["draft_review"] = review_md
            state.external_state["review_sources"] = metadata["source_refs"]
            state.external_state["review_covered_topics"] = metadata["covered_topics"]
            state.external_state["comparison_done"] = metadata["comparison_done"]
            state.external_state["recommendation_made"] = metadata["recommendation_made"]
            state.external_state["used_memory_entries"] = metadata["used_memory_entries"] or state.external_state["used_memory_entries"]
            state.external_state["used_stale_memory"] = metadata["used_stale_memory"]
            state.record_trace("act", "draft_created", "Drafted the final review from current evidence.", action_name="synthesize", evidence_refs=metadata["source_refs"])
            state.snapshot(memory_store.diagnostics(), {"drafted": True})
            continue

        if proposal.action_name == "assemble_citations":
            cite_obs = toolbox.assemble_citations(state.external_state["review_sources"], state.step)
            tool_observations.append(cite_obs)
            state.external_state["final_citations"] = list(state.external_state["review_sources"])
            state.record_trace("act", "tool_call", cite_obs.summary, action_name="assemble_citations", evidence_refs=state.external_state["final_citations"])
            state.snapshot(memory_store.diagnostics(), {"citations": state.external_state["final_citations"]})
            continue

        if proposal.action_name == "stop":
            mark_plan_step(plan, "final_verify", "done")
            mark_plan_step(plan, "stop_or_handoff", "done")
            verification = evaluate_progress(task_spec, state, stage="final")
            state.record_verification(verification)
            state.record_trace("verify", "verification_result", "Checked final success criteria before stopping.", action_name="stop", evidence_refs=verification.evidence_refs, data={"blocking_issues": verification.blocking_issues})
            state.snapshot(memory_store.diagnostics(), {"verified": verification.satisfied, "drafted": bool(state.external_state["draft_review"])})
            if verification.satisfied:
                return _finalize_result(profile, state, plan, memory_store, tool_observations, state.external_state["draft_review"], None)
            outcome = "clarification_needed" if any(issue.startswith("goal: unresolved ambiguity") for issue in verification.blocking_issues) else "handoff"
            handoff = _make_handoff(task_spec, outcome, verification.blocking_issues, boundary=bool(task_spec.boundary_topics))
            return _finalize_result(profile, state, plan, memory_store, tool_observations, None, handoff)

    state.next_step()
    verification = evaluate_progress(task_spec, state, stage="final")
    state.record_verification(verification)
    state.record_trace("stop", "max_steps_reached", "Stopped because the bounded step budget was exhausted.", action_name="stop", evidence_refs=verification.evidence_refs, data={"blocking_issues": verification.blocking_issues})
    state.snapshot(memory_store.diagnostics(), {"max_steps": True})
    handoff = _make_handoff(task_spec, "handoff", verification.blocking_issues)
    return _finalize_result(profile, state, plan, memory_store, tool_observations, None, handoff)


def run_variant(task_spec, variant: str, run_dir: str | Path) -> RunResult:
    if variant not in VALID_VARIANTS:
        raise ValueError(f"Unsupported variant: {variant}")
    run_dir = Path(run_dir)
    run_dir.mkdir(parents=True, exist_ok=True)
    if variant == "model_only":
        return run_model_only(task_spec, run_dir / "notes")
    if variant == "scripted_pipeline":
        return run_scripted_pipeline(task_spec, _make_toolbox(run_dir))
    profile = VARIANT_PROFILES[variant]
    return _run_profile(task_spec, profile, run_dir)
