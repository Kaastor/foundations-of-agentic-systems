# Report Template

## 1. Task

Restate the task-specification question for the ambiguous request.

## 2. Candidate Options Or Initial Answer

Provide two plausible task-spec candidates for the ambiguous request.
They may come from:

- your own drafting
- a chatbot
- a coding agent

Summarize them clearly inside the report.

## 3. Comparison Criteria

State how you will judge the task specs.
Include:

- explicit goals
- constraints
- success criteria
- stop or handoff conditions
- ambiguity handling

## 4. Evidence

Cite the committed task-spec examples and any relevant book or slice reading.

## 5. Implementation Lens

Inspect one or both of:

- [goals.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/src/m2a/goals.py)
- [schemas.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/src/m2a/schemas.py)

Explain in 3-5 sentences which task-spec fields the implementation treats as operationally necessary and how that helps you judge the candidate specs.

## 6. Critique

Explain what each candidate gets right and wrong.
Be explicit about:

- under-specified fields
- overconfident assumptions
- missing stop or handoff logic

## 7. Revision Or Selected Option

Present one revised final task specification.
You may use bullet points or a compact structured format.

## 8. Final Justification

Explain why your revised spec is more control-ready than the alternatives.

## 9. Uncertainty Or Remaining Weakness

Name one ambiguity or boundary that should remain explicit.
