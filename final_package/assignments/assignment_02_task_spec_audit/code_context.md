# Code Context

## Main Sources

- [AA-S02.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/slices/AA-S02.md)
- [ambiguous_request task_spec.json](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/spec_review/ambiguous_request/task_spec.json)
- [clear_bounded_review task_spec.json](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/spec_review/clear_bounded_review/task_spec.json)
- [boundary_handoff task_spec.json](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/spec_review/boundary_handoff/task_spec.json)

## Required Implementation Lens

Inspect one or both of:

- [goals.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/src/m2a/goals.py)
- [schemas.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/src/m2a/schemas.py)

Focus on:

- how `build_task_spec` turns a request into explicit fields
- how `TaskSpec.validate()` makes some of those fields non-optional for downstream control

## Optional Workflow

```bash
poetry run m2a spec-review data/requests/ambiguous_request.txt --out-dir scratch/spec-ambiguous
```

## Strong Evidence Sources

- compare the three committed `task_spec.json` files
- inspect the corresponding `task_spec.md` files for wording choices

## No-Coding-Agent Path

You can complete the assignment entirely from the committed examples and docs.
For the implementation lens, read only the named source module(s) and connect them to the committed `task_spec.json` artifacts.
