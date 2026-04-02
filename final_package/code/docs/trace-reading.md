# Reading traces

The repository is only useful if you can reconstruct why a run behaved the way it did.

Every run emits a shared artifact set. Read them in this order.

## 1. `task_spec.json`

This tells you what the system was actually trying to satisfy.

Before judging a run, check:

- requested topics
- paper budget
- comparison/recommendation requirements
- ambiguity flags
- handoff conditions
- boundaries

## 2. `plan.json`

This is the declared intended structure of the run. It is not proof that the run succeeded. It is the intended control skeleton.

## 3. `trace.jsonl`

This is the causal spine. Every record includes:

- `step`
- `phase`
- `event_type`
- `action_name`
- `message`
- `evidence_refs`
- `data`

The important question is not “what did it say?” but “what changed because of this step?”

The main phases are:

| Phase | Meaning |
| --- | --- |
| `observe` | ingest task or world state |
| `think` | propose the next bounded action |
| `act` | call a tool or draft content |
| `update` | change internal state without a tool call |
| `verify` | check blockers against explicit criteria |
| `stop` | produce a bounded final outcome |

## 4. `state_snapshots.jsonl`

State snapshots answer the question that traces do not: where does the information live now?

Each snapshot separates:

- `active_context`
- `external_state`
- `memory_summary`
- `world_outcomes`
- `unresolved_issues`

This is where the repository makes context != state != memory visible.

## 5. `tool_observations.jsonl`

These are the grounded observations that later decisions can cite. Search, read, note-writing, and citation assembly all show up here with explicit inputs and outputs.

## 6. `memory_log.jsonl`

This is append-only memory history. It includes:

- the policy snapshot
- seed memories
- writes
- retrievals
- forgetting events

Do not confuse this file with current active context. A memory item can exist without being active in the current step.

## 7. `verification.jsonl` and `stop_decision.json`

These two files tell you whether the run actually met the contract.

A run can only end with normal success if the final verification has no blocking issue.

That rule is enforced in code and tests.

## Minimal reading pattern

When a run surprises you, use this pattern:

1. read the final blockers in `stop_decision.json`
2. find the corresponding `verify` event in `trace.jsonl`
3. inspect the nearby tool observations and memory events
4. confirm which state snapshot still held the unresolved issue

## Worked examples

Good places to practice:

- successful in-scope comparison run:
  `examples/compare_architectures/clear_bounded_review/variants/capstone_agent/`
- stale-memory blocker:
  `examples/run_review/capstone_stale_memory_harms/`
- clarification outcome:
  `examples/run_review/capstone_ambiguous_request/`
