# Report Template

## 1. Task

State the classification question in one or two sentences.

## 2. Candidate Options Or Initial Answer

Provide:

- your initial AI-assisted or human first-pass classification
- at least one plausible alternative classification

## 3. Comparison Criteria

List the criteria you will use to judge whether a variant counts as agentic in this course.

Use criteria such as:

- explicit control loop
- goal-directed adjustment
- dependence on observations
- bounded stop or handoff logic

## 4. Evidence

Cite:

- `comparison_matrix.md`
- at least one `trace.jsonl`
- one supporting conceptual source from the reading or architecture docs

## 5. Implementation Lens

Inspect one of the following:

- [baselines.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/src/m2a/baselines.py)
- [control.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/src/m2a/control.py)

Explain in 3-5 sentences which implementation difference best helps account for the classification difference you defend.

## 6. Critique

Explain:

- what your initial answer got right
- what it overstated or left unsupported
- which comparison mattered most

## 7. Revision Or Selected Option

State your revised or selected classification.

## 8. Final Justification

Give a short defended answer to:

`What is the minimum architectural difference that justifies calling a system agentic here?`

Also state one thing that is **not** sufficient by itself.

## 9. Uncertainty Or Remaining Weakness

Name one edge case or ambiguity that remains.
