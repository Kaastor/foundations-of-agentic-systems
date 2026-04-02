# Teacher Grading Guide

This package is designed for:

- report-only submissions
- large-cohort grading
- coding-agent first pass
- teacher spot-check on flagged cases

Use this together with:

- [shared_submission_rules.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/assignments/shared_submission_rules.md)
- [shared_rubric.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/assignments/shared_rubric.md)
- the current assignment folder

## Operating Model

The grader should not try to detect whether AI was used.
AI use is expected.

The grader should evaluate:

- whether the report shows evidence-backed judgment
- whether the implementation lens is relevant and explanatory
- for later assignments, whether the reported code change is bounded and supported by before/after evidence
- whether the student compared plausible options rather than taking the first answer
- whether critique and revision are real
- whether the final conclusion is bounded and justified

## Recommended Grading Workflow

1. Read the assignment’s [description.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/assignments/assignment_01_agentic_classification/description.md) and [teacher_notes.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/assignments/assignment_01_agentic_classification/teacher_notes.md) for the relevant folder.
2. Read the student report.
3. Score against [shared_rubric.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/assignments/shared_rubric.md).
4. Check whether cited artifact references are plausible and relevant.
5. Flag for teacher review if the report triggers the spot-check rules.

## Common Weak Patterns

- strong-sounding prose with almost no artifact evidence
- repeating the book vocabulary without applying it to the assignment materials
- naming a source file with no explanation of what it contributes
- claiming a code change helped without showing a before/after difference
- critique that is only cosmetic
- revision that is actually a restatement
- final conclusions that are broader than the evidence supports

## Strong-But-AI-Generated Reports

If a report appears AI-generated but is substantively strong, grade the substance.

Do not penalize:

- clean structure
- fluent prose
- high-quality drafting

Do penalize:

- weak evidence
- fake critique
- unsupported confidence

## First-Pass Coding-Agent Grading Prompt

Use this instruction block as a first-pass grader:

```text
You are grading one report for a course on agent architectures.

Use these sources:
- the current assignment's description.md
- the current assignment's teacher_notes.md
- shared_submission_rules.md
- shared_rubric.md
- the student report

Grade only the substance visible in the report.
Do not penalize AI use.
Focus on:
- task understanding
- evidence quality
- implementation lens
- comparison and critique
- revision or bounded selection
- final justification and uncertainty

Return:
1. criterion-by-criterion scores with one short justification each
2. total score out of 12
3. 2-4 sentence overall feedback
4. whether this report should be flagged for teacher spot-check, and why

Flag if:
- evidence is missing or suspicious
- the report contradicts its cited artifacts
- the conclusion is much stronger than the evidence
- you are uncertain between adjacent scores
```

## Assignment-Specific Use

Each assignment folder contains local grading nuances in `teacher_notes.md`.
Read those before grading that assignment.
