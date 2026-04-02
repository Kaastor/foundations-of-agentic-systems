# Failure Diagnosis: boundary_handoff

## Variant-by-variant diagnosis

- `model_only` failed with diagnoses `stop, goal, grounding, action` and blockers: boundary: request includes deferred topics and requires a boundary note, goal: unresolved ambiguity prevents a bounded review, grounding: final review lacks sufficient citations, goal: comparison requested but output does not compare alternatives.
- `scripted_pipeline` failed with diagnoses `stop, goal, grounding` and blockers: boundary: request includes deferred topics and requires a boundary note, goal: unresolved ambiguity prevents a bounded review, grounding: final review lacks sufficient citations, goal: comparison requested but output does not compare alternatives, goal: recommendation requested but output does not defend one.
- `tool_rich_memoryless` failed with diagnoses `stop, goal, grounding` and blockers: boundary: request includes deferred topics and requires a boundary note, goal: unresolved ambiguity prevents a bounded review, grounding: final review lacks sufficient citations, goal: comparison requested but output does not compare alternatives, goal: recommendation requested but output does not defend one.
- `memory_rich_tool_poor` failed with diagnoses `goal, grounding, stop` and blockers: goal: unresolved ambiguity prevents a bounded review, grounding: final review lacks sufficient citations, goal: comparison requested but output does not compare alternatives, goal: recommendation requested but output does not defend one.
- `capstone_agent` failed with diagnoses `goal, grounding, stop` and blockers: goal: unresolved ambiguity prevents a bounded review, grounding: final review lacks sufficient citations, goal: comparison requested but output does not compare alternatives, goal: recommendation requested but output does not defend one.

## Cross-variant misconceptions surfaced

- Tool calls do not imply task success; some variants found papers but still failed final verification.
- More memory is not always better; stale recall can create a memory-specific blocker.
- Planning earns its keep only when it changes evidence collection or stop behavior.
