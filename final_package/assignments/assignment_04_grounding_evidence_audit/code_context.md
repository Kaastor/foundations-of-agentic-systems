# Code Context

## Main Sources

- [architecture.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/architecture.md)
- [running-case-literature-review-assistant.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/running-case-literature-review-assistant.md)
- [AA-S05.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/slices/AA-S05.md)
- [capstone_agent tool_observations.jsonl](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/compare_architectures/clear_bounded_review/variants/capstone_agent/tool_observations.jsonl)
- [scripted_pipeline tool_observations.jsonl](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/compare_architectures/clear_bounded_review/variants/scripted_pipeline/tool_observations.jsonl)
- [capstone_ambiguous_request verification.jsonl](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/run_review/capstone_ambiguous_request/verification.jsonl)
- [starter_claim_set.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/assignments/assignment_04_grounding_evidence_audit/starter_claim_set.md)

## Required Implementation Lens

Inspect one or both of:

- [tools.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/src/m2a/tools.py)
- [feedback.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/src/m2a/feedback.py)

Focus on:

- how tool contracts and `ToolObservation` outputs make some claims inspectable
- how `evaluate_progress` turns missing citations, topic gaps, or unresolved ambiguity into explicit blockers

## Optional Workflow

```bash
poetry run m2a run-review data/expected_task_specs/clear_bounded_review.json --variant capstone_agent --out-dir scratch/run-tools
```

## No-Coding-Agent Path

You can complete the assignment entirely from the committed artifacts above.
If you want a fixed starting point, use the starter claim set instead of generating your own.
For the implementation lens, read only the named module(s) and connect them to the observed tool or verification artifacts.
