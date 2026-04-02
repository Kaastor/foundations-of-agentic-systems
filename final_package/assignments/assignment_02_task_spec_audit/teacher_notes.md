# Teacher Notes

## Why It Is Here

This assignment makes the task contract visible before students learn more about traces, tools, and memory.

## What A Strong Report Should Contain

- two genuinely different candidate task specs
- evidence-based comparison to the committed artifacts
- a revised final task contract that keeps ambiguity explicit
- a short implementation lens connecting required fields to `build_task_spec` or `TaskSpec.validate()`
- real discussion of stop or handoff conditions

## Common Weak Patterns

- treating a request paraphrase as a task spec
- guessing user intent instead of marking ambiguity
- forgetting stop conditions

## Grading Nuance

Students do not need to match the committed task spec exactly.
They do need to produce a version that is defensibly more control-ready than a vague request.
The implementation lens should stay focused on why the fields matter, not on restating the whole module.
