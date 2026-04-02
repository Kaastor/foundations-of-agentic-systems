# Code Context

## Main Sources

- [AA-S07.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/slices/AA-S07.md)
- [AA-S08.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/slices/AA-S08.md)
- [AA-S09.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/slices/AA-S09.md)
- [capstone-synthesis-guide.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/capstone-synthesis-guide.md)
- [misconceptions-and-failure-modes.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/misconceptions-and-failure-modes.md)
- [deferred-topics-and-boundaries.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/docs/deferred-topics-and-boundaries.md)
- [clear_bounded_review comparison](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/compare_architectures/clear_bounded_review)
- [boundary_handoff comparison](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/compare_architectures/boundary_handoff)
- [boundary_note.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/compare_architectures/boundary_handoff/boundary_note.md)

## Required Intervention

In your own working copy, edit:

- [comparison.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/src/m2a/comparison.py)

Make this exact bounded stress-test change inside `_render_recommendation()`:

- change the `if task_spec.boundary_topics:` line inside `_render_recommendation()` to `if False and task_spec.boundary_topics:`

This temporarily disables the special `none_in_scope` recommendation branch so you can observe what the recommender does without it.
Do not change the earlier boundary condition in the scoring logic.

## Required Implementation Lens

Inspect one or more of:

- [comparison.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/src/m2a/comparison.py)
- [feedback.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/src/m2a/feedback.py)

Focus on:

- how architecture assessments and fit recommendations are rendered from observed run outcomes
- how blocking issues and boundaries shape bounded recommendations
- why the recommendation layer still needs explicit boundary handling even when comparison evidence exists

## Required Workflows

```bash
poetry run m2a compare-architectures data/expected_task_specs/boundary_handoff.json --out-dir scratch/compare-boundary-before
# make the bounded change in comparison.py
poetry run m2a compare-architectures data/expected_task_specs/boundary_handoff.json --out-dir scratch/compare-boundary-after
```

You may use the committed [clear_bounded_review comparison](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/compare_architectures/clear_bounded_review) as the stable in-scope reference.

## Strong Evidence Sources

- compare `scratch/compare-boundary-before/fit_recommendation.md` to `scratch/compare-boundary-after/fit_recommendation.md`
- compare `boundary_note.md` before and after, even if it stays unchanged
- compare one failure or comparison artifact if helpful

## No-Coding-Agent Path

A coding agent is not required.
The intervention is a single manual edit that can be made in any editor.
Use a chatbot if helpful, but verify the actual before/after recommendation artifacts yourself.
