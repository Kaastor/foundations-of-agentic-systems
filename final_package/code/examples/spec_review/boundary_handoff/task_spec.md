# Task Spec: boundary_handoff

## Request

Review current industry benchmarks for live web retrieval agents, compare vector ranking internals, and recommend a production deployment architecture with observability.

## Structured fields

- Paper budget: 3 to 5
- Comparison mode: True
- Recommendation required: True
- Max steps: 20

## Goals

- Produce a bounded literature review using only the shipped local corpus.
- Compare the requested alternatives rather than listing papers independently.
- Defend one bounded architecture recommendation with evidence.

## Constraints

- Use local corpus papers only; no live retrieval or external APIs.
- Keep the run deterministic and inspectable.
- Use between 3 and 5 papers unless a valid handoff occurs.

## Subgoals

- Formalize the review request into explicit goals, constraints, and stop rules.
- Collect evidence from the local paper corpus.
- Synthesize a citation-backed review or emit a bounded handoff outcome.
- Surface the tradeoff between the compared architecture choices.

## Success criteria

- Every requested topic is covered by evidence from at least one local paper.
- The final review includes citations assembled from the local corpus.
- The final review contains a direct comparison of the requested alternatives.
- The final review contains an evidence-backed recommendation.

## Stop criteria

- Stop successfully only when all success criteria are satisfied.
- Emit a clarification or handoff outcome when ambiguity or scope boundaries block a safe review.
- If blocking issues remain after bounded replanning, stop with an explicit bounded failure or handoff.

## Requested topics

- None

## Ambiguity flags

- No explicit topical focus was provided.
- The domain is broad enough that the local corpus may not match the user's intent.

## Clarification questions

- Which agent architecture concepts should the review cover?

## Handoff conditions

- Ambiguity remains unresolved after task formalization.
- The request depends on out-of-scope topics such as RL, IR internals, live retrieval, symbolic planning, or operations.
- The local corpus cannot support the requested evidence within the paper budget.

## Boundary topics

- ir_internals
- live_retrieval
- operations

## Assumptions

- No explicit paper budget was given; defaulted to 3 to 5 local papers.
