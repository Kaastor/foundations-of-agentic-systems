# Code Context

## Main Sources

- [architecture-variants.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/architecture-variants.md)
- [AA-S01.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/slices/AA-S01.md)
- [comparison_matrix.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/compare_architectures/clear_bounded_review/comparison_matrix.md)
- [fit_recommendation.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/compare_architectures/clear_bounded_review/fit_recommendation.md)

## Required Implementation Lens

Inspect one of:

- [baselines.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/src/m2a/baselines.py)
- [control.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/src/m2a/control.py)

Focus on:

- how `run_model_only` or `run_scripted_pipeline` differs from the control-loop logic in `control.py`
- what that difference reveals about fixed flow versus observation-dependent next-step selection

## Strong Evidence Sources

- variant traces under:
  [clear_bounded_review variants](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/compare_architectures/clear_bounded_review/variants)
- especially:
  - [model_only trace.jsonl](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/compare_architectures/clear_bounded_review/variants/model_only/trace.jsonl)
  - [scripted_pipeline trace.jsonl](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/compare_architectures/clear_bounded_review/variants/scripted_pipeline/trace.jsonl)
  - [capstone_agent trace.jsonl](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/compare_architectures/clear_bounded_review/variants/capstone_agent/trace.jsonl)

## Optional Workflow

```bash
poetry run m2a compare-architectures data/expected_task_specs/clear_bounded_review.json --out-dir scratch/compare-clear
```

## No-Coding-Agent Path

You can complete the assignment entirely from the committed comparison artifacts and docs above.
For the implementation lens, read only one small named source module and explain what it clarifies.
