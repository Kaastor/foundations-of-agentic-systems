# Running case: the literature-review assistant

The whole repository is anchored on one bounded application: an offline literature-review assistant over a small local corpus.

That choice is deliberate. It is big enough to expose goals, state, memory, planning, tools, verification, and stop or handoff. It is small enough to stay deterministic and inspectable.

## What the environment is

The “environment” is not the web. It is the shipped corpus in `data/corpus/papers.jsonl` plus four local tools:

- `search_corpus`
- `read_paper`
- `write_note`
- `assemble_citations`

This is enough to make tool semantics concrete without introducing retrieval infrastructure or vendor APIs.

## What the assistant is asked to do

Across fixtures, the assistant must:

- turn a raw request into a bounded task specification
- gather evidence from the corpus
- synthesize a review with citations, or emit a clarification/handoff outcome
- compare architectures when the workflow calls for it

The request fixtures are intentionally varied:

| Fixture | Why it exists |
| --- | --- |
| `clear_bounded_review.txt` | canonical in-scope comparison case |
| `ambiguous_request.txt` | forces clarification rather than silent guessing |
| `tradeoff_memory_vs_tools.txt` | makes the canonical tradeoff pair explicit |
| `tool_success_not_task_success.txt` | surfaces that a successful search is not task success |
| `over_planning_overhead.txt` | shows that smaller tasks can favor simpler architectures |
| `stale_memory_harms.txt` | shows that stale recall can become a blocker |
| `boundary_handoff.txt` | forces an explicit boundary note |

## Why this case teaches agent architecture well

A literature review is a good teaching case because success depends on more than fluent text.

A successful run needs:

- an explicit task contract
- evidence collection
- state tracking across steps
- optional memory for continuity
- planning or selection logic
- verification that checks the *review*, not just the tool call
- the ability to stop, clarify, or hand off

That maps directly onto the track’s deep core.

## What this case teaches correctly

- `Production-close habit`: a successful review depends on explicit goals, grounded evidence, verification, and bounded stopping logic rather than fluent text alone.
- `Production-close habit`: tool outputs matter because they provide inspectable observations that later verification and synthesis can use.
- `Production-close habit`: the same task can justify different architectures depending on task size, ambiguity, memory needs, and evidence requirements.

## What this case trims on purpose

- `Teaching simplification`: the corpus is synthetic and fixed.
- `Teaching simplification`: search is lexical and local rather than a full retrieval stack.
- `Teaching simplification`: clarification is emitted as an artifact instead of happening through an interactive user loop.
- `Teaching simplification`: the “model” behavior is deterministic so the learner can isolate architecture effects.

`Do transfer`: the need for explicit task contracts, evidence-bearing tools, and bounded control.

`Do not overgeneralize`: the exact corpus shape, search mechanism, and deterministic simulation.

## Corpus design

The corpus is synthetic and simplified by design. Each paper card has:

- a citation ID
- title and year
- abstract
- keywords
- canonical topic tags
- one or more findings
- limitations

The papers are not there to teach literature retrieval. They are there to teach how architecture turns evidence into bounded behavior.

## What is intentionally *not* in this case

Not included:

- live web search
- ranking infrastructure
- embedding stores
- benchmark harnesses
- production observability
- policy learning

Those are real topics, but they would shift the repository away from the central architectural question.
