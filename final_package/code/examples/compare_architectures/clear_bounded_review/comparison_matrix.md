# Architecture Comparison Matrix: clear_bounded_review

| Variant | Outcome | Tool calls | Papers read | Citations | Memory events | Reflection events | Diagnoses |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| model_only | handoff | 0 | 0 | 0 | 0 | 0 | grounding, goal, action, stop |
| scripted_pipeline | success | 6 | 4 | 4 | 0 | 0 | none |
| tool_rich_memoryless | handoff | 6 | 4 | 2 | 0 | 0 | planning, grounding, stop |
| memory_rich_tool_poor | success | 9 | 4 | 4 | 21 | 0 | none |
| capstone_agent | success | 10 | 4 | 4 | 17 | 0 | none |
