from __future__ import annotations

from .feedback import evaluate_progress
from .planning import build_initial_plan, mark_plan_step, topic_query
from .schemas import HandoffNote, RunResult, StopDecision
from .state import RunState
from .synthesis import draft_review
from .tools import ToolBox


def _finish_result(variant: str, state: RunState, plan, verification, final_review_md: str | None = None, handoff_note: HandoffNote | None = None) -> RunResult:
    if verification.satisfied:
        stop = StopDecision(
            step=state.step,
            outcome="success",
            rationale="All final checks passed.",
            satisfied_success_criteria=list(state.task_spec.success_criteria),
            remaining_blockers=[],
            handoff_required=False,
            boundary_topics=[],
        )
    else:
        stop = StopDecision(
            step=state.step,
            outcome=handoff_note.outcome if handoff_note else "bounded_failure",
            rationale="Blocking verification issues remained at stop time.",
            satisfied_success_criteria=[],
            remaining_blockers=list(verification.blocking_issues),
            handoff_required=handoff_note is not None,
            boundary_topics=list(state.task_spec.boundary_topics),
        )
    return RunResult(
        variant=variant,
        plan=plan,
        trace=state.trace,
        state_snapshots=state.state_snapshots,
        memory_log=[],
        tool_observations=[] if variant == "model_only" else state.external_state.get("tool_observations", []),
        stop_decision=stop,
        verification_results=state.verification_results,
        run_summary={
            "read_papers": [paper["citation_id"] for paper in state.external_state["read_papers"]],
            "final_citations": list(state.external_state["final_citations"]),
            "reflection_actions": list(state.external_state["reflection_actions"]),
            "used_stale_memory": state.external_state["used_stale_memory"],
        },
        final_review_md=final_review_md,
        handoff_note=handoff_note,
    )


def run_model_only(task_spec, note_dir) -> RunResult:
    plan = build_initial_plan(task_spec, "model_only")
    state = RunState(task_spec, "model_only")
    state.next_step()
    mark_plan_step(plan, "prepare", "done")
    state.record_trace("observe", "task_received", "Received structured task spec.")
    state.snapshot(memory_summary={"policy": None, "stored_entries": 0}, world_outcomes={"drafted": False})
    state.next_step()
    state.record_trace("think", "direct_generation", "Generated a direct review without tools or memory.", action_name="generate")
    guessed_topics = task_spec.requested_topics or ["agent architectures"]
    fake_papers = [
        {
            "citation_id": "UNGROUNDED",
            "title": "Ungrounded synthesis",
            "year": 0,
            "topic_tags": guessed_topics,
            "findings": ["The model-only baseline can produce fluent text but not evidence-backed review claims."],
        }
    ]
    final_review_md, metadata = draft_review(task_spec, "model_only", fake_papers)
    state.external_state["draft_review"] = final_review_md
    state.external_state["review_sources"] = []
    state.external_state["review_covered_topics"] = guessed_topics
    state.external_state["comparison_done"] = metadata["comparison_done"]
    state.external_state["recommendation_made"] = metadata["recommendation_made"]
    state.snapshot(memory_summary={"policy": None, "stored_entries": 0}, world_outcomes={"drafted": True})
    state.next_step()
    verification = evaluate_progress(task_spec, state, stage="final")
    state.record_verification(verification)
    state.record_trace("verify", "verification_result", "Model-only baseline failed grounding checks.", evidence_refs=verification.evidence_refs, data={"blocking_issues": verification.blocking_issues})
    state.snapshot(memory_summary={"policy": None, "stored_entries": 0}, world_outcomes={"drafted": True, "verified": verification.satisfied})
    handoff_note = None
    if not verification.satisfied:
        handoff_note = HandoffNote(
            outcome="handoff",
            summary="The model-only baseline can summarize the request but cannot satisfy evidence-backed review criteria without tools.",
            missing_information=list(verification.blocking_issues),
            next_actions=["Use a tool-enabled variant that can inspect local papers and assemble citations."],
            boundary_topics=[],
        )
    return _finish_result("model_only", state, plan, verification, None if handoff_note else final_review_md, handoff_note)


def run_scripted_pipeline(task_spec, toolbox: ToolBox) -> RunResult:
    plan = build_initial_plan(task_spec, "scripted_pipeline")
    state = RunState(task_spec, "scripted_pipeline")
    state.external_state["tool_observations"] = []
    state.next_step()
    state.record_trace("observe", "task_received", "Received structured task spec.")
    state.snapshot(memory_summary={"policy": None, "stored_entries": 0}, world_outcomes={"drafted": False})
    if task_spec.ambiguity_flags:
        state.next_step()
        verification = evaluate_progress(task_spec, state, stage="final")
        state.record_verification(verification)
        handoff = HandoffNote(
            outcome="clarification_needed",
            summary="The scripted pipeline does not rewrite ambiguous requests into a narrower task before acting.",
            missing_information=list(task_spec.clarification_questions),
            next_actions=["Run spec-review first or use capstone_agent for bounded clarification."],
            boundary_topics=[],
        )
        return _finish_result("scripted_pipeline", state, plan, verification, None, handoff)
    query = " ".join(topic_query(topic) for topic in task_spec.requested_topics) or task_spec.normalized_request
    state.next_step()
    mark_plan_step(plan, "collect_evidence", "done")
    search_obs = toolbox.search_corpus(query, task_spec.paper_budget_max, state.step)
    state.external_state["tool_observations"].append(search_obs)
    state.record_trace("act", "tool_call", search_obs.summary, action_name="search_corpus", evidence_refs=search_obs.source_refs)
    state.external_state["search_queries"].append(query)
    selected = search_obs.output["results"][: task_spec.paper_budget_max]
    state.external_state["selected_papers"] = [item["citation_id"] for item in selected]
    state.snapshot(memory_summary={"policy": None, "stored_entries": 0}, world_outcomes={"selected": state.external_state["selected_papers"]})
    for result in selected:
        state.next_step()
        read_obs = toolbox.read_paper(result["citation_id"], state.step)
        state.external_state["tool_observations"].append(read_obs)
        paper = read_obs.output
        state.external_state["read_papers"].append(paper)
        state.record_trace("act", "tool_call", read_obs.summary, action_name="read_paper", evidence_refs=[paper["citation_id"]])
        state.push_observation_refs([paper["citation_id"]], window=task_spec.paper_budget_max)
        state.snapshot(memory_summary={"policy": None, "stored_entries": 0}, world_outcomes={"last_read": paper["citation_id"]})
    state.next_step()
    intermediate = evaluate_progress(task_spec, state, stage="intermediate")
    state.record_verification(intermediate)
    state.record_trace("verify", "verification_result", "Scripted pipeline checked coverage once with no replanning.", evidence_refs=intermediate.evidence_refs, data={"blocking_issues": intermediate.blocking_issues})
    papers = state.external_state["read_papers"]
    final_review_md, metadata = draft_review(task_spec, "scripted_pipeline", papers)
    state.external_state["draft_review"] = final_review_md
    state.external_state["review_sources"] = metadata["source_refs"]
    state.external_state["review_covered_topics"] = metadata["covered_topics"]
    state.external_state["comparison_done"] = metadata["comparison_done"]
    state.external_state["recommendation_made"] = metadata["recommendation_made"]
    state.next_step()
    cite_obs = toolbox.assemble_citations(metadata["source_refs"], state.step) if metadata["source_refs"] else None
    if cite_obs:
        state.external_state["tool_observations"].append(cite_obs)
        state.external_state["final_citations"] = metadata["source_refs"]
        state.record_trace("act", "tool_call", cite_obs.summary, action_name="assemble_citations", evidence_refs=metadata["source_refs"])
    state.next_step()
    verification = evaluate_progress(task_spec, state, stage="final")
    state.record_verification(verification)
    state.record_trace("verify", "verification_result", "Scripted pipeline made one final pass without corrective action.", evidence_refs=verification.evidence_refs, data={"blocking_issues": verification.blocking_issues})
    state.snapshot(memory_summary={"policy": None, "stored_entries": 0}, world_outcomes={"drafted": True, "verified": verification.satisfied})
    handoff = None
    if not verification.satisfied:
        handoff = HandoffNote(
            outcome="handoff",
            summary="The scripted pipeline completed its fixed steps but could not resolve the remaining blockers.",
            missing_information=list(verification.blocking_issues),
            next_actions=["Use a replanning variant if missing coverage or grounding blockers remain."],
            boundary_topics=list(task_spec.boundary_topics),
        )
    return _finish_result("scripted_pipeline", state, plan, verification, None if handoff else final_review_md, handoff)
