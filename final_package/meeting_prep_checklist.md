# Meeting Prep Checklist

Use this file as the operational checklist for teaching the course one meeting at a time without losing the big picture.

All shell commands below are intended to be run from:

- [code](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code)

The structure is the same for every meeting:

- `7 days before`
- `48 hours before`
- `30 minutes before`
- `do not forget`

## Before The Course Starts

### Before Meeting 1: Course Launch Tasks

Complete the course-launch tasks before the first class:

- fill the local course-instance fields in [lesson_0.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/assignments/lesson_0.md)
- create the `Teams` space or channel
- set up the student submission workflow:
  GitHub Classroom, one student repo per student, or another agreed repository path
- prepare the student template repo or starter repo structure if you are using one
- verify the expected submission structure:
  one `submission.md` per assignment
- decide and publish meeting dates, times, and room or remote-link information
- decide and publish assignment deadlines
- decide grading weights if you are using them
- send students the package access path
- send students [STUDENT_SETUP.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/STUDENT_SETUP.md)
- send students [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf) with the instruction:
  Chapter 1, pages 7-15 before `Meeting 1`
- verify the repository once yourself with the one-time dry run below

### Minimum Mental Map Before Meeting 1

Before the first class, make sure you can explain:

- the central question:
  `How does a generative model become a bounded, goal-directed agentic system through architecture?`
- the six-meeting spine:
  `model -> task -> loop/state/trace -> action/tools/grounding -> memory/planning -> feedback/stop/comparison`
- the running case:
  one offline literature-review assistant reused across the whole course
- the key architecture contrasts:
  `model_only`, `scripted_pipeline`, `tool_rich_memoryless`, `memory_rich_tool_poor`, `capstone_agent`
- the operational workflows:
  `m2a spec-review`, `m2a run-review`, `m2a compare-architectures`
- the course boundaries:
  not RL, not IR internals, not symbolic planning formalisms, not deployment, not vendor frameworks

### What To Read And Internalize Before Meeting 1

From the book, read:

- [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf)
  Chapter 1, pages 7-15
- [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf)
  Chapter 2, pages 16-23
- [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf)
  Chapter 3, pages 24-31

Then skim for map-building:

- [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf)
  Chapters 4-9, pages 32-85

From the assignment layer, read:

- [assignments/README.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/assignments/README.md)

From the code and docs, read:

- [code/README.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/README.md)
- [code/docs/architecture.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/architecture.md)
- [code/docs/architecture-variants.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/architecture-variants.md)
- [code/docs/bridge-refresh.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/bridge-refresh.md)
- [code/docs/trace-reading.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/trace-reading.md)
- [code/docs/running-case-literature-review-assistant.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/running-case-literature-review-assistant.md)
- [code/docs/misconceptions-and-failure-modes.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/misconceptions-and-failure-modes.md)
- [code/docs/deferred-topics-and-boundaries.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/deferred-topics-and-boundaries.md)

Inspect:

- [code/examples/compare_architectures/clear_bounded_review](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/compare_architectures/clear_bounded_review)

Internalize:

- how the assignment model fits the course structure and what students actually submit
- the difference between model-only, scripted, and agentic control
- the difference among request, task spec, trace, state, memory, and evidence
- how the running case reappears in every workflow
- that the course is bounded and architectural rather than a general GenAI survey

### One-Time Dry Run

Run once before the course starts:

```bash
poetry install
poetry run m2a spec-review data/requests/clear_bounded_review.txt --out-dir scratch/spec-clear
poetry run m2a run-review data/expected_task_specs/clear_bounded_review.json --variant capstone_agent --out-dir scratch/run-clear
poetry run m2a compare-architectures data/expected_task_specs/clear_bounded_review.json --out-dir scratch/compare-clear
```

## Meeting 1

### 7 days before

- Read Meeting 1 in [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/meeting_plan.md)
- Read [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf)
  Chapter 1, pages 7-15
- Read [AA-S01.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/slices/AA-S01.md)
- Read [architecture-variants.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/architecture-variants.md)
- Inspect [clear_bounded_review](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/compare_architectures/clear_bounded_review)

### 48 hours before

- Run `poetry run m2a compare-architectures data/expected_task_specs/clear_bounded_review.json --out-dir scratch/compare-clear`
- Decide which contrast you will show first:
  `model_only` vs `scripted_pipeline` or `scripted_pipeline` vs `capstone_agent`
- Prepare one sentence for:
  `agency is architectural control structure, not mere tool use`

### 30 minutes before

- Reopen `scratch/compare-clear/comparison_matrix.md` or the committed comparison example
- Reopen one short `trace.jsonl` from the chosen contrast
- Decide the single exit question:
  `What makes this system agentic rather than merely interactive or scripted?`

### Do not forget

- Misconception to surface:
  `an agent is just a chatbot with a better prompt`

## Meeting 2

### 7 days before

- Read Meeting 2 in [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/meeting_plan.md)
- Read [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf)
  Chapter 2, pages 16-23
- Read [AA-S02.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/slices/AA-S02.md)
- Inspect [clear_bounded_review spec example](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/spec_review/clear_bounded_review)
- Inspect [ambiguous_request spec example](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/spec_review/ambiguous_request)

### 48 hours before

- Run `poetry run m2a spec-review data/requests/clear_bounded_review.txt --out-dir scratch/spec-clear`
- Run `poetry run m2a spec-review data/requests/ambiguous_request.txt --out-dir scratch/spec-ambiguous`
- Compare the two `task_spec.json` files yourself
- Prepare one sentence for:
  `a request is not yet a control-ready task specification`

### 30 minutes before

- Reopen both `task_spec.json` files
- Decide which field difference you will show first:
  ambiguity, stop conditions, or scope constraints
- Decide the single exit question:
  `What changes when a vague request becomes an explicit task spec?`

### Do not forget

- Misconception to surface:
  `good prompting alone is enough`

## Meeting 3

### 7 days before

- Read Meeting 3 in [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/meeting_plan.md)
- Read [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf)
  Chapter 3, pages 24-31
- Optional preview: Chapter 4, pages 32-35
- Read [trace-reading.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/trace-reading.md)
- Read [AA-S03.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/slices/AA-S03.md)
- Inspect one `trace.jsonl` and matching `state_snapshots.jsonl`

### 48 hours before

- Run `poetry run m2a run-review data/expected_task_specs/clear_bounded_review.json --variant capstone_agent --out-dir scratch/run-clear`
- Compare `trace.jsonl` and `state_snapshots.jsonl`
- Prepare one sentence for:
  `trace shows what happened; state shows where information lives`

### 30 minutes before

- Reopen one short trace segment and matching state snapshot
- Decide the single exit question:
  `What is the difference between context, state, and trace?`

### Do not forget

- Misconception to surface:
  `context window equals memory`

## Meeting 4

### 7 days before

- Read Meeting 4 in [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/meeting_plan.md)
- Read [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf)
  Chapter 5, pages 42-49
- Read [architecture.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/architecture.md)
- Read [running-case-literature-review-assistant.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/running-case-literature-review-assistant.md)
- Read [AA-S05.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/slices/AA-S05.md)
- Inspect [capstone_agent tool observations](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/compare_architectures/clear_bounded_review/variants/capstone_agent/tool_observations.jsonl)

### 48 hours before

- Run `poetry run m2a run-review data/expected_task_specs/clear_bounded_review.json --variant capstone_agent --out-dir scratch/run-tools`
- Inspect how search, read, note, and citation actions differ
- Prepare one sentence for:
  `tool calls matter only if their observations affect later control`

### 30 minutes before

- Reopen `tool_observations.jsonl`
- Decide which tool contract example you will show first
- Decide the single exit question:
  `What counts as evidence rather than mere output?`

### Do not forget

- Misconception to surface:
  `any tool use makes a system agentic`

## Meeting 5

### 7 days before

- Read Meeting 5 in [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/meeting_plan.md)
- Read [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf)
  Chapter 4, pages 32-41
- Read [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf)
  Chapter 6, pages 50-58
- Read [AA-S04.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/slices/AA-S04.md) and [AA-S06.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/slices/AA-S06.md)
- Inspect [greedy_trap.json](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/data/planning/greedy_trap.json)
- Inspect [memory_log.jsonl](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/run_review/capstone_stale_memory_harms/memory_log.jsonl)
- Inspect [plan.json](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/run_review/capstone_stale_memory_harms/plan.json)

### 48 hours before

- Run `poetry run m2a run-review data/expected_task_specs/stale_memory_harms.json --variant capstone_agent --out-dir scratch/run-memory`
- Run `poetry run m2a compare-architectures data/expected_task_specs/tradeoff_memory_vs_tools.json --out-dir scratch/compare-tradeoff`
- Prepare one sentence for:
  `memory is policy plus content, and planning is a selective control choice`

### 30 minutes before

- Reopen one memory event and one plan artifact
- Decide the single exit question:
  `What should persist, and when does planning help rather than hurt?`

### Do not forget

- Misconceptions to surface:
  `more memory is always better`
  `planning is always better`

## Meeting 6

### 7 days before

- Read Meeting 6 in [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/meeting_plan.md)
- Read [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf)
  Chapter 7, pages 59-66
- Read [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf)
  Chapter 8, pages 67-77
- Read [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf)
  Chapter 9, pages 78-85
- Optional capstone preview: Chapter 10, pages 86-98
- Read [AA-S07.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/slices/AA-S07.md), [AA-S08.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/slices/AA-S08.md), and [AA-S09.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/slices/AA-S09.md)
- Read [capstone-synthesis-guide.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/capstone-synthesis-guide.md)
- Read [misconceptions-and-failure-modes.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/misconceptions-and-failure-modes.md)
- Read [deferred-topics-and-boundaries.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/deferred-topics-and-boundaries.md)
- Inspect [verification.jsonl](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/run_review/capstone_ambiguous_request/verification.jsonl)
- Inspect [clear_bounded_review comparison](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/compare_architectures/clear_bounded_review)
- Inspect [boundary_handoff comparison](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/compare_architectures/boundary_handoff)

### 48 hours before

- Run `poetry run m2a compare-architectures data/expected_task_specs/clear_bounded_review.json --out-dir scratch/compare-clear`
- Run `poetry run m2a compare-architectures data/expected_task_specs/boundary_handoff.json --out-dir scratch/compare-boundary`
- Prepare one sentence for:
  `correct systems do not only know how to continue; they know when to stop, hand off, or recommend a different architecture`

### 30 minutes before

- Reopen `fit_recommendation.md` and `boundary_note.md`
- Decide which contrast you will show first:
  in-scope recommendation or out-of-scope boundary outcome
- Decide the single exit question:
  `How do we compare designs without collapsing into slogans?`

### Do not forget

- Misconceptions to surface:
  `reflection automatically improves correctness`
  `stopping and handoff are only production concerns`
  `one architecture is always best`
