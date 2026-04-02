# Assumptions

The repository makes a few narrow assumptions to stay deterministic and teachable.

## Assumptions made intentionally

- The “model” is simulated locally through deterministic code. The repository teaches architecture, not provider integration.
- The literature corpus is synthetic and shipped in-tree to avoid network and licensing issues.
- “Search” means lexical search over the local corpus, not live retrieval.
- Clarification and handoff are emitted as artifacts rather than interactive prompts.
- The default environment is offline and CPU-only.
- Text-first artifacts are preferred over binary or hidden state.

## Small inferences made from underspecification

- The paper budget is parsed from the request when possible and defaults to `3..5` otherwise.
- When the request does not name an audience, the repository assumes a beginner who wants structural literacy.
- The capstone comparison workflow is allowed to recommend `none_in_scope` when a task is dominated by deferred topics.

## Which assumptions should transfer

- `Do transfer`: keep default assumptions explicit and visible in code, artifacts, and docs.
- `Do transfer`: prefer bounded outcomes such as clarification or handoff over pretending the system can solve deferred topics.
- `Do transfer`: make comparison logic willing to recommend no in-scope completion architecture when the evidence says so.

## Which assumptions are teaching simplifications

- `Do not overgeneralize`: the deterministic model simulator.
- `Do not overgeneralize`: the synthetic local corpus.
- `Do not overgeneralize`: lexical search as the only retrieval mechanism.
- `Do not overgeneralize`: artifact-based clarification instead of an interactive user channel.

## What these assumptions are *not*

They are not hidden product requirements. They are visible design choices that keep the repository within its intended scope.
