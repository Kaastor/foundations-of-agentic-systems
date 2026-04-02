# Assignment 6: Architecture Boundary Stress Test

**Linked meeting:** [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/meeting_plan.md)
Meeting 6: “How Does It Stay Bounded and How Do We Compare Designs?”

**Why this assignment exists:** Students should leave the course able to compare architectures, respect boundaries, and defend a bounded recommendation rather than a slogan.

**Main reasoning-loop emphasis:** `generate -> compare -> critique -> revise -> justify`

**Expected time:** `4 hours`

**Coding level:** `one bounded code change plus rerun`

## Brief

Write a final recommendation memo answering:

`For one in-scope case and one boundary-stressing case, which architecture is the best fit, what should it do, and where should it stop or hand off?`

Then perform one boundary stress test in your own working copy of [comparison.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/src/m2a/comparison.py):

- temporarily disable the boundary-only branch in `_render_recommendation()` by changing the `if task_spec.boundary_topics:` line inside that function to `if False and task_spec.boundary_topics:`

Important:

- make the change inside `_render_recommendation()`, not in the earlier scoring logic
- this is the boundary check that currently produces the `none_in_scope` recommendation

Run the boundary comparison before and after that change, then judge whether the modified recommender is better or worse than the original bounded behavior.

Your final report must do both:

- defend a normal architecture recommendation for the in-scope case
- explain what the boundary stress test reveals about why explicit `none_in_scope` handling exists
- explain whether the boundary note should change or remain stable after the stress test

## Submission Checklist

- address one in-scope case and one boundary case
- cite comparison, failure, and boundary artifacts
- run and cite a `before` and `after` boundary comparison
- make the exact bounded change in `comparison.py`
- inspect at least one named source module and explain how it shapes recommendation or boundary behavior
- critique the stressed recommendation layer, not only the original one
- provide a bounded final recommendation with explicit stop or handoff logic
