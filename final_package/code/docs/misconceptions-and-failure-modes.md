# Misconceptions and failure modes

The repository is built so learners can *see* common agent-architecture mistakes rather than just read warnings about them.

## Misconception map

| Misconception | Where it surfaces | What to look for |
| --- | --- | --- |
| “An agent is just a chatbot with a prompt.” | `model_only` vs `scripted_pipeline` vs `capstone_agent` in `examples/compare_architectures/clear_bounded_review/` | same task, radically different control structure and outcomes |
| “Any tool use makes a system agentic.” | `scripted_pipeline` vs `capstone_agent` | both use tools, but only one can use verification as a control input |
| “Context window = memory.” | `tool_rich_memoryless` vs `capstone_agent` | both read papers, only one retains evidence durably for synthesis |
| “More memory is always better.” | `examples/run_review/capstone_stale_memory_harms/` and `data/requests/stale_memory_harms.txt` | stale memory becomes an explicit blocker |
| “Planning is always better than direct generation.” | `data/requests/over_planning_overhead.txt` and `tests/test_comparison.py` | the repository can recommend `scripted_pipeline` on the small task |
| “Reflection automatically improves correctness.” | `src/m2a/feedback.py`, `tests/test_feedback.py` | reflection actions are only emitted when blockers exist |
| “A successful tool call means the task succeeded.” | `data/requests/tool_success_not_task_success.txt` and `verification.jsonl` artifacts | search/read success does not bypass final verification |
| “Stopping and handoff are production-only concerns.” | `examples/run_review/capstone_ambiguous_request/`, `examples/compare_architectures/boundary_handoff/` | clarification and boundary notes are valid bounded outcomes |
| “You need RL or symbolic planning first.” | `docs/deferred-topics-and-boundaries.md` | the repo stays within architectural scope and says so explicitly |

## Structural failure categories

The comparison workflow diagnoses failures by structure, not benchmark score.

The categories are:

- `goal`
- `planning`
- `memory`
- `grounding`
- `action`
- `stop`

Those labels come from `src/m2a/feedback.py` and are emitted into comparison outputs.

## Why this matters pedagogically

A learner should leave this repository able to read an unfamiliar system description and reconstruct:

- the goal representation
- the loop
- the state and memory split
- the tool interfaces
- the verification signals
- the stop or handoff logic

That requires explicit failure modes, not just happy-path demos.
