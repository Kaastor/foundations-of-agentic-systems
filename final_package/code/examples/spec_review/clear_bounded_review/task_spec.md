# Task Spec: clear_bounded_review

## Request

Prepare a beginner-friendly literature review about planning, memory, and grounding in offline literature-review assistants. Use only the local corpus. Compare lightweight planning with more explicit architecture choices. Cite 4 local papers and stop only when each requested topic is covered with evidence.

## Structured fields

- Paper budget: 4 to 4
- Comparison mode: True
- Recommendation required: False
- Max steps: 20

## Goals

- Produce a bounded literature review using only the shipped local corpus.
- Explain memory with explicit evidence.
- Explain grounding with explicit evidence.
- Explain planning with explicit evidence.
- Compare the requested alternatives rather than listing papers independently.

## Constraints

- Use local corpus papers only; no live retrieval or external APIs.
- Keep the run deterministic and inspectable.
- Use between 4 and 4 papers unless a valid handoff occurs.

## Subgoals

- Formalize the review request into explicit goals, constraints, and stop rules.
- Collect evidence from the local paper corpus.
- Synthesize a citation-backed review or emit a bounded handoff outcome.
- Surface the tradeoff between the compared architecture choices.

## Success criteria

- Every requested topic is covered by evidence from at least one local paper.
- The final review includes citations assembled from the local corpus.
- The final review contains a direct comparison of the requested alternatives.

## Stop criteria

- Stop successfully only when all success criteria are satisfied.
- Emit a clarification or handoff outcome when ambiguity or scope boundaries block a safe review.
- If blocking issues remain after bounded replanning, stop with an explicit bounded failure or handoff.

## Requested topics

- memory
- grounding
- planning

## Ambiguity flags

- None

## Clarification questions

- None

## Handoff conditions

- Ambiguity remains unresolved after task formalization.
- The request depends on out-of-scope topics such as RL, IR internals, live retrieval, symbolic planning, or operations.
- The local corpus cannot support the requested evidence within the paper budget.

## Boundary topics

- None

## Assumptions

- The intended audience is a beginner seeking structural literacy rather than domain specialization.
