# Student Setup

This file covers only:

- local setup,
- running the repository,
- knowing which assignments require reruns.

For deadlines and submission workflow, use the logistics communicated during `Lesson 0` and on `Teams`.
For the assignment model, use [assignments/README.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/assignments/README.md).

## Minimum Setup

You need:

- `python3.11+`,
- a local copy of the course package,
- a text editor.

Helpful but not required:

- `poetry`,
- `git`,
- a coding agent.

## Standard Setup Path

Run these commands from [code](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code):

```bash
poetry install
poetry run m2a spec-review data/requests/clear_bounded_review.txt --out-dir scratch/spec-clear
poetry run m2a run-review data/expected_task_specs/clear_bounded_review.json --variant capstone_agent --out-dir scratch/run-clear
poetry run m2a compare-architectures data/expected_task_specs/clear_bounded_review.json --out-dir scratch/compare-clear
```

## One-Command Setup Check

```bash
poetry run m2a compare-architectures data/expected_task_specs/clear_bounded_review.json --out-dir scratch/setup-check
```

If setup is working, you should get:

- `scratch/setup-check/comparison_matrix.md`
- `scratch/setup-check/fit_recommendation.md`

## Read-Only vs Rerun Path

Assignments 1-4 can be completed from committed artifacts under [code/examples](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples).

Assignments 5-6 require reruns and one bounded code change.

## Assignment-Specific Runtime Expectations

- Assignments 1-4:
  - committed artifacts are enough,
  - rerunning is optional
- Assignment 5:
  - one bounded code change in [control.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/src/m2a/control.py)
  - one `before/after` rerun
- Assignment 6:
  - one bounded code change in [comparison.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/src/m2a/comparison.py)
  - one `before/after` rerun

## Safe Pattern For Assignments 5-6

1. copy the repository or save your current state,
2. run the `before` command,
3. make the exact bounded edit from the assignment,
4. run the `after` command,
5. compare only the artifacts named in the assignment,
6. revert the local change after finishing, or keep a separate working copy.

## If Setup Fails

Ask on `Teams` first.

If you need a fallback runtime path:

```bash
PYTHONPATH=src python3.13 -m m2a.cli ...
```
