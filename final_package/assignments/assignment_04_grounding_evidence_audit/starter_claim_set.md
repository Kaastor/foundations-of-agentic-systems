# Starter Claim Set

Use this claim set if you want a fixed starting point for Assignment 4.

You may also generate your own claim set with a chatbot, but this starter version is a good default for beginners.

## Claim Set To Audit

1. The capstone agent clearly proves that reflection automatically improves review quality.
2. The final review is well grounded because the system used several tools.
3. The run has enough evidence to support claims about memory and planning.
4. The system verified that every major claim in the final review had citation support.
5. The run shows that tool use alone is enough to make the answer trustworthy.
6. The final answer is bounded because the verification step passed.

## How To Use This Starter Set

For each claim, decide whether it is:

- grounded
- weakly supported
- unsupported

Then revise the overall answer into a more bounded and evidence-backed version.

## Recommended Evidence To Check

- [tool_observations.jsonl](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/compare_architectures/clear_bounded_review/variants/capstone_agent/tool_observations.jsonl)
- [verification.jsonl](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/run_review/capstone_ambiguous_request/verification.jsonl)
- [final_review.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/code/examples/run_review/capstone_stale_memory_harms/final_review.md)

## Why This Starter Set Exists

The point is not to trap you.
The point is to give you one concrete starting point so you can practice the audit skill itself:

- compare the claims
- check the artifacts
- separate evidence from confidence
- produce a narrower final judgment

