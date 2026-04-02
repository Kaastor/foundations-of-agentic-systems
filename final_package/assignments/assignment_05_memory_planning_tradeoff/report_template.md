# Report Template

## 1. Task

State the intervention question in one sentence.

## 2. Candidate Options Or Initial Answer

Provide:

- your prediction for what the memory-policy change will do
- at least one plausible alternative prediction

## 3. Comparison Criteria

Use criteria such as:

- boundedness
- stale-memory risk
- stale recall risk
- verification outcome
- evidence quality
- whether the system becomes safer or less safe after the intervention

## 4. Before Evidence

Cite:

- the `before` run's `memory_log.jsonl`
- the `before` run's `verification.jsonl`
- the `before` run's `stop_decision.json`
- one supporting artifact such as `plan.json` or `final_review.md`

## 5. Intervention And Implementation Lens

Inspect:

- [control.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/src/m2a/control.py)
- [memory.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/src/m2a/memory.py)

Report:

- the exact file you changed
- the exact change you made
- your predicted effect before rerunning

Then explain in 3-5 sentences why that policy change should matter.

## 6. After Evidence And Critique

Cite:

- the `after` run's `memory_log.jsonl`
- the `after` run's `verification.jsonl`
- the `after` run's `stop_decision.json`

Then explain:

- what changed
- what did not change
- whether your original prediction held up

## 7. Revision Or Selected Option

State your final judgment:

- improved bounded behavior
- harmed bounded behavior
- or only weakly changed bounded behavior

## 8. Final Justification

Explain why the before/after evidence supports your judgment, and what this teaches about memory policy in relation to planning and verification.

## 9. Uncertainty Or Remaining Weakness

Name one remaining risk or one thing your intervention did not resolve.
