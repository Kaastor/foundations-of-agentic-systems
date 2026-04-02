# Code Context

## Main Sources

- [AA-S04.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/slices/AA-S04.md)
- [AA-S06.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/slices/AA-S06.md)
- [greedy_trap.json](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/data/planning/greedy_trap.json)
- [capstone_stale_memory_harms memory_log.jsonl](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/run_review/capstone_stale_memory_harms/memory_log.jsonl)
- [capstone_stale_memory_harms plan.json](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/run_review/capstone_stale_memory_harms/plan.json)
- [tradeoff comparison_matrix.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/compare_architectures/clear_bounded_review/comparison_matrix.md)

## Required Intervention

In your own working copy, edit:

- [control.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/src/m2a/control.py)

Make this exact bounded change inside `_memory_policy_for()` for `capstone_agent`:

- change `stale_after_steps=5` to `stale_after_steps=1`
- change `allow_stale_recall=False` to `allow_stale_recall=True`

This is a deliberate stress test of stale-memory handling.

## Required Implementation Lens

Inspect:

- [control.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/src/m2a/control.py)
- [memory.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/src/m2a/memory.py)

Focus on:

- how the capstone memory policy is configured
- how stale entries are marked and retrieved
- why a looser stale-recall policy can change downstream verification or stop behavior

## Required Workflows

```bash
poetry run m2a run-review data/expected_task_specs/stale_memory_harms.json --variant capstone_agent --out-dir scratch/run-memory-before
# make the bounded change in control.py
poetry run m2a run-review data/expected_task_specs/stale_memory_harms.json --variant capstone_agent --out-dir scratch/run-memory-after
```

## Strong Evidence Sources

- compare `scratch/run-memory-before/memory_log.jsonl` to `scratch/run-memory-after/memory_log.jsonl`
- compare `scratch/run-memory-before/verification.jsonl` to `scratch/run-memory-after/verification.jsonl`
- compare `scratch/run-memory-before/stop_decision.json` to `scratch/run-memory-after/stop_decision.json`
- optionally compare `plan.json` and `final_review.md`

## No-Coding-Agent Path

A coding agent is not required.
The intervention is a small manual edit that can be made in any editor.
Use a chatbot if helpful, but verify the actual before/after artifacts yourself.
