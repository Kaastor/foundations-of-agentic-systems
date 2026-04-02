# Assignment 3: Trace Localization Report

**Linked meeting:** [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/meeting_plan.md)
Meeting 3: “What Does the System Carry Across Steps?”

**Why this assignment exists:** Students need to learn how to read a run causally instead of reacting only to the final output.

**Main reasoning-loop emphasis:** `compare -> critique -> justify`

**Expected time:** `4 hours`

**Coding level:** `bounded code-reading`, with optional workflow rerun

## Brief

Use the ambiguous-request run to answer:

`Where does the earliest decisive evidence appear that this run should end in clarification or handoff rather than continued autonomous progress?`

You must compare:

- trace events
- state snapshots
- stop or handoff artifacts

Also inspect one small implementation surface that helps explain why these evidence sources are separated the way they are.

Your report should identify the earliest strong evidence point and explain why earlier steps were not yet sufficient.

## Submission Checklist

- identify one specific earliest evidence point
- compare trace and state rather than using only one
- use at least one stop, handoff, or verification artifact
- inspect at least one named source module and explain what it reveals about trace or state structure
- explain why an earlier step was still insufficient
- end with a bounded causal claim, not only a narrative summary
