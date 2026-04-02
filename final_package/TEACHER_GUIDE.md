# Teacher Guide

## Purpose And Teacher Mode

This guide is for a working professional teaching this course as a side job while still deepening their own understanding of agentic systems.

The operating assumption is not full-field mastery before the course starts. It is disciplined preparation from a stable map.

Use this guide together with:

- [README.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/README.md)
- [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/meeting_plan.md)
- [meeting_prep_checklist.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/meeting_prep_checklist.md)
- [code](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code)

All shell commands below are intended to be run from:

- [code](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code)

## Core Teaching Thesis

Teach from a stable map. Learn the next layer just in time.

For this course, that means:

- know the central question before Meeting 1
- know the six-meeting dependency spine before Meeting 1
- know the running literature-review case before Meeting 1
- know the course boundaries before Meeting 1
- then learn each meeting in depth one step ahead of students

That is enough to teach responsibly. Trying to master every adjacent field first is not.

## What The Teacher Must Know Before Meeting 1

Before the first class, you should be able to state clearly:

1. The central question:
   `How does a generative model become a bounded, goal-directed agentic system through architecture?`
2. The six-meeting spine:
   `model -> task -> loop/state/trace -> action/tools/grounding -> memory/planning -> feedback/stop/comparison`
3. The running case:
   one bounded literature-review assistant reused across the whole course
4. The main contrasts:
   `model_only`, `scripted_pipeline`, `tool_rich_memoryless`, `memory_rich_tool_poor`, `capstone_agent`
5. The three operational workflows:
   `m2a spec-review`, `m2a run-review`, `m2a compare-architectures`
6. The boundaries:
   not RL, not IR internals, not symbolic planning formalisms, not deployment, not vendor orchestration frameworks

If those six things are stable in your head, you can prepare locally one meeting ahead.

## What To Read And Internalize Before Meeting 1

### From The Book

Read first:

- [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf)
  Chapter 1, pages 7-15
- [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf)
  Chapter 2, pages 16-23
- [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf)
  Chapter 3, pages 24-31

Skim next for map-building, not mastery:

- [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf)
  Chapter 4, pages 32-41
- [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf)
  Chapter 5, pages 42-49
- [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf)
  Chapter 6, pages 50-58
- [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf)
  Chapter 7, pages 59-66
- [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf)
  Chapter 8, pages 67-77
- [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf)
  Chapter 9, pages 78-85

Optional capstone preview:

- [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf)
  Chapter 10, pages 86-98

Internalize from the book:

- the difference between a model, a scripted workflow, and an agentic system
- why a request is not yet a control-ready task specification
- why context, state, trace, and memory are different
- why tool use only matters when it changes what can be observed and justified
- why stopping and handoff are part of correctness, not cleanup
- that the course is architectural and bounded, not a survey of all GenAI

### From The Code, Docs, And Artifacts

Read these first:

- [assignments/README.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/assignments/README.md)
- [code/README.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/README.md)
- [code/docs/architecture.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/architecture.md)
- [code/docs/architecture-variants.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/architecture-variants.md)
- [code/docs/bridge-refresh.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/bridge-refresh.md)
- [code/docs/trace-reading.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/trace-reading.md)
- [code/docs/running-case-literature-review-assistant.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/running-case-literature-review-assistant.md)
- [code/docs/misconceptions-and-failure-modes.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/misconceptions-and-failure-modes.md)
- [code/docs/deferred-topics-and-boundaries.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/deferred-topics-and-boundaries.md)

Inspect at least one committed artifact set:

- [code/examples/compare_architectures/clear_bounded_review](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/compare_architectures/clear_bounded_review)

Internalize from the code and artifacts:

- how the assignment model fits the course structure and what students actually submit
- what each workflow emits and why those artifacts matter
- where to show students a contrast instead of giving a verbal explanation
- that traces, state snapshots, tool observations, memory logs, and stop decisions are distinct evidence surfaces
- that the repository is teaching one recurring system, not six disconnected mini-demos
- which failures are structural and visible in artifacts rather than only in final output quality

## One-Time Pre-Course Setup Or Dry Run

Run this once before the course starts:

```bash
poetry install
poetry run m2a spec-review data/requests/clear_bounded_review.txt --out-dir scratch/spec-clear
poetry run m2a run-review data/expected_task_specs/clear_bounded_review.json --variant capstone_agent --out-dir scratch/run-clear
poetry run m2a compare-architectures data/expected_task_specs/clear_bounded_review.json --out-dir scratch/compare-clear
```

The goal of this dry run is not deep implementation mastery. The goal is to feel the package as a runnable system and see where the main artifacts live.

## Operating Rhythm

- Before the course starts: build the mental map above, read the core book sections, read the core code docs, and do one dry run.
- 7 days before a meeting: reread the relevant section of [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/meeting_plan.md), then read the cited book pages and code docs.
- 48 hours before a meeting: run the one workflow you plan to anchor class on and inspect the exact artifact you will show.
- 30 minutes before class: reopen the anchor artifact, the exit question, and the misconception you want to surface.
- After class: write 3-5 lines on what students misunderstood and whether the anchor artifact worked.

## In-Class Method

Use the same instructional shape each meeting:

1. State the meeting question.
2. Name the one key distinction.
3. Show one artifact or one contrast.
4. Ask students to predict before you explain.
5. Reveal what the system did.
6. Explain the behavior causally from the artifact.
7. Connect it back to the six-meeting spine.
8. Name what is still deferred.

Keep these stable across the whole course:

- the central question
- the meeting order
- the running case
- the architecture contrasts
- the course boundaries

## Handling Unknowns, Scope Drift, And Updates

When you do not know something:

- if it is central to the current meeting, defer briefly and return with an artifact-backed answer
- if it is adjacent, say so explicitly
- if it is outside scope, mark it out of scope rather than improvising

Good pattern:

`That is related, but this course is about architecture, bounded control, and inspectable traces, not RL policy learning or deployment operations.`

For AI specifically, keep two layers separate:

- stable core:
  model vs system, task specs, loops, state, memory, planning, tools, verification, stopping, boundaries
- changing surface:
  products, framework landscape, latest examples, news-driven relevance framing

Update the surface when useful. Do not rebuild the spine around it mid-course.

## Teacher Red Flags

You are underprepared if:

- you cannot explain why this meeting comes before the next one
- you cannot name the one anchor artifact for the meeting
- you are showing outputs you did not inspect yourself
- you are using general AI chatter to fill structural gaps
- you are answering out-of-scope questions as if they were inside the course
- you are treating tool use or reflection as magic instead of as explicit architecture

If that happens, return to:

- [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/meeting_plan.md)
- [meeting_prep_checklist.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/meeting_prep_checklist.md)

## Course-Specific Use Notes

Use the package in this order:

1. [README.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/README.md)
2. [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/meeting_plan.md)
3. the pre-course readings and dry run in this guide
4. [meeting_prep_checklist.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/meeting_prep_checklist.md) for meeting-by-meeting execution

The package is strongest when you teach through:

- exact distinctions
- deterministic artifacts
- bounded comparisons
- explicit boundaries

It is weakest when you teach it as:

- prompt folklore
- product commentary
- vague AI trends
- a survey of everything adjacent to agentic systems
