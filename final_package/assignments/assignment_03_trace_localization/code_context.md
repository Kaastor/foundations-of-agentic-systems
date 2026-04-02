# Code Context

## Main Sources

- [trace-reading.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/trace-reading.md)
- [AA-S03.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/slices/AA-S03.md)
- [capstone_ambiguous_request trace.jsonl](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/run_review/capstone_ambiguous_request/trace.jsonl)
- [capstone_ambiguous_request state_snapshots.jsonl](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/run_review/capstone_ambiguous_request/state_snapshots.jsonl)
- [capstone_ambiguous_request stop_decision.json](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/run_review/capstone_ambiguous_request/stop_decision.json)
- [capstone_ambiguous_request handoff_note.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/run_review/capstone_ambiguous_request/handoff_note.md)

## Required Implementation Lens

Inspect one or both of:

- [state.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/src/m2a/state.py)
- [control.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/src/m2a/control.py)

Focus on:

- how `RunState` records trace events separately from state snapshots
- how the control loop decides when clarification or handoff becomes the next bounded move

## Optional Workflow

```bash
poetry run m2a run-review data/expected_task_specs/ambiguous_request.json --variant capstone_agent --out-dir scratch/run-ambiguous
```

## No-Coding-Agent Path

You can complete the assignment entirely from the committed run-review artifacts.
For the implementation lens, inspect only the named module(s) and explain how they illuminate the artifact split.
