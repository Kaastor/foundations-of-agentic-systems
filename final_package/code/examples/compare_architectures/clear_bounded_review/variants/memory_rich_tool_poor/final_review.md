# Literature Review: clear_bounded_review

Variant: `memory_rich_tool_poor`

## Scope

Prepare a beginner-friendly literature review about planning, memory, and grounding in offline literature-review assistants. Use only the local corpus. Compare lightweight planning with more explicit architecture choices. Cite 4 local papers and stop only when each requested topic is covered with evidence.

## Findings by topic

### Memory
Tool-rich memoryless systems find fresh evidence but often lose earlier support during synthesis. [P10-ToolRichNoMemory]

### Grounding
Tool interfaces change both capability and what evidence can ground the final review. [P05-InterfaceGrounding]

### Planning
Tool-rich memoryless systems find fresh evidence but often lose earlier support during synthesis. [P10-ToolRichNoMemory]

## Comparison

Goal Contracts for Bounded Literature Review Assistants emphasizes goals, stopping, while Tool-Rich, Memoryless Review Systems emphasizes tools, memory. The architecture choice therefore depends on whether the task is bottlenecked by evidence access, retention, or control discipline. [P02-GoalContract] [P10-ToolRichNoMemory]

## Memory use

- Used fresh episodic memory `M04-tool-interfaces` tied to P05-InterfaceGrounding, P10-ToolRichNoMemory.
- Used fresh note memory `note-9-7` tied to P10-ToolRichNoMemory.

## Citations

- [P02-GoalContract] Goal Contracts for Bounded Literature Review Assistants (2024)
- [P05-InterfaceGrounding] Interface Contracts and Evidence Linking for Local Research Tools (2024)
- [P08-BoundedStop] BoundedStop: Clarification and Handoff as Correct Agent Outcomes (2024)
- [P10-ToolRichNoMemory] Tool-Rich, Memoryless Review Systems (2024)
