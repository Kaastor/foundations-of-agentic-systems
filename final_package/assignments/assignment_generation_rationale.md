# Assignment Generation Rationale

## Key Assumptions

- one assignment per meeting
- `4` hours per assignment
- report-only submission
- large cohort grading with coding-agent first pass
- chatbot use treated as normal
- coding agents encouraged but not required
- bounded mandatory code editing in Assignments 5 and 6 only
- one bounded implementation lens per assignment

## How The Meeting Plan Constrained The Design

The package follows [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/meeting_plan.md) exactly.

That forced:

- one conceptual centerpiece per assignment
- exact use of the selected book pages
- exact reuse of the repository artifacts already named in the meeting plan
- preservation of the six-meeting dependency order

## How The Hour Budget And Coding Profile Changed The Design

Because the target is `4` hours and the submission is report-only:

- assignments are artifact-grounded rather than code-heavy
- Assignments 1-4 use bounded code-reading and optional reruns
- Assignments 5-6 add one bounded code change plus a before/after rerun
- most of the student effort goes into comparison, critique, and justification

This keeps the package completable without a coding agent while still allowing deeper engagement for students who have one.

## How The Package Preserves Learning Value Under AI-Heavy Use

The package assumes AI use and designs around it directly.

The assignments do not reward first-answer production.
They reward:

- option generation
- fair comparison
- connecting artifacts to implementation
- evidence-backed critique
- bounded revision
- justified final judgment

That operationalizes the repo philosophy in [ASSIGNMENTS_PHILOSOPHY.md](/home/przemek/Biznes/Kursy/course-generation/ASSIGNMENTS_PHILOSOPHY.md).

## Remaining Tradeoffs

- report-only submissions are operationally efficient, but they reduce direct visibility into student process
- the implementation lens improves concept-to-code transfer, but it adds a small reading burden for novices
- optional reruns help stronger students gather better evidence, but they are not required, so the floor remains artifact analysis
- bounded code changes in the last two assignments add stronger intervention learning, but also increase operational complexity slightly
- the rubric favors bounded judgment over broad creativity, which is appropriate for this course but narrows open-ended exploration
