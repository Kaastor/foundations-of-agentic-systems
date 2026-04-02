# Literature Review: clear_bounded_review

Variant: `capstone_agent`

## Scope

Prepare a beginner-friendly literature review about planning, memory, and grounding in offline literature-review assistants. Use only the local corpus. Compare lightweight planning with more explicit architecture choices. Cite 4 local papers and stop only when each requested topic is covered with evidence.

## Findings by topic

### Memory
Memory must include retrieval and forgetting policy, not just storage. Unchecked stale memory makes reflection look more reliable than the evidence supports. [P04-MemoryPolicy] [P13-StaleReflection]

### Grounding
Coverage-aware selection and topic-specific replanning recover missing evidence better than top-k greedy selection. [P14-CoverageTrap]

### Planning
Lightweight decomposition adds enough structure for small review tasks without heavy formal planning. Coverage-aware selection and topic-specific replanning recover missing evidence better than top-k greedy selection. [P06-PlanSketch] [P14-CoverageTrap]

## Comparison

MemoryPolicy: When Notes Help and When They Mislead emphasizes memory, state, while CoverageTrap: Why Greedy Paper Selection Misses Evidence Linking emphasizes planning, grounding. The architecture choice therefore depends on whether the task is bottlenecked by evidence access, retention, or control discipline. [P04-MemoryPolicy] [P14-CoverageTrap]

## Memory use

- Used fresh note memory `note-8-6` tied to P14-CoverageTrap.
- Used fresh note memory `note-10-8` tied to P06-PlanSketch.

## Citations

- [P04-MemoryPolicy] MemoryPolicy: When Notes Help and When They Mislead (2024)
- [P06-PlanSketch] PlanSketch: Lightweight Decomposition for Small Review Tasks (2023)
- [P13-StaleReflection] Stale Reflection Notes and the Cost of Unchecked Recall (2023)
- [P14-CoverageTrap] CoverageTrap: Why Greedy Paper Selection Misses Evidence Linking (2024)
