# Assignment 5: Memory Policy Intervention Report

**Linked meeting:** [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/meeting_plan.md)
Meeting 5: “What Should Persist and When Should It Plan?”

**Why this assignment exists:** Students need to reason about memory and planning as selective control choices rather than default upgrades.

**Main reasoning-loop emphasis:** `generate -> compare -> critique -> revise -> justify`

**Expected time:** `4 hours`

**Coding level:** `one bounded code change plus rerun`

## Brief

Use the stale-memory case to answer:

`What happens when you loosen the capstone agent’s stale-memory policy, and what does the resulting behavior teach you about bounded memory design?`

In your own working copy of the repository, make this exact bounded intervention in [control.py](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/src/m2a/control.py):

- for `capstone_agent`, change `stale_after_steps=5` to `stale_after_steps=1`
- for `capstone_agent`, change `allow_stale_recall=False` to `allow_stale_recall=True`

Then:

1. run the stale-memory workflow once before the change
2. make the change
3. run the same workflow again
4. compare the before and after artifacts
5. judge whether the intervention improved or harmed bounded behavior

Your final report should explain what changed in the memory evidence and what that reveals about memory policy. You should also say whether planning alone would have been enough to solve the problem you observed.

## Submission Checklist

- state your predicted effect before changing the code
- run and cite a `before` and `after` artifact set
- make the exact bounded change in `control.py`
- compare at least `memory_log.jsonl`, `verification.jsonl`, and `stop_decision.json`
- inspect at least one named source module and explain what policy tradeoff it encodes
- judge whether the intervention improved, harmed, or only weakly changed bounded behavior
- explain one remaining risk
