# Task Spec: ambiguous_request

## Request

Can you review the important papers about agents and tell me what matters?

## Structured fields

- Paper budget: 3 to 5
- Comparison mode: False
- Recommendation required: False
- Max steps: 20

## Goals

- Produce a bounded literature review using only the shipped local corpus.

## Constraints

- Use local corpus papers only; no live retrieval or external APIs.
- Keep the run deterministic and inspectable.
- Use between 3 and 5 papers unless a valid handoff occurs.

## Subgoals

- Formalize the review request into explicit goals, constraints, and stop rules.
- Collect evidence from the local paper corpus.
- Synthesize a citation-backed review or emit a bounded handoff outcome.

## Success criteria

- Every requested topic is covered by evidence from at least one local paper.
- The final review includes citations assembled from the local corpus.

## Stop criteria

- Stop successfully only when all success criteria are satisfied.
- Emit a clarification or handoff outcome when ambiguity or scope boundaries block a safe review.
- If blocking issues remain after bounded replanning, stop with an explicit bounded failure or handoff.

## Requested topics

- None

## Ambiguity flags

- No explicit topical focus was provided.
- The request uses the ambiguous phrase 'important'.
- The request uses the ambiguous phrase 'what matters'.
- The domain is broad enough that the local corpus may not match the user's intent.

## Clarification questions

- Which agent architecture concepts should the review cover?

## Handoff conditions

- Ambiguity remains unresolved after task formalization.
- The request depends on out-of-scope topics such as RL, IR internals, live retrieval, symbolic planning, or operations.
- The local corpus cannot support the requested evidence within the paper budget.

## Boundary topics

- None

## Assumptions

- No explicit paper budget was given; defaulted to 3 to 5 local papers.
- Because no topics were explicit, the system will prefer clarification over guessing.
