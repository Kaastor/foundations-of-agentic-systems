from __future__ import annotations

from .memory import MemoryItem


def draft_review(task_spec, variant: str, papers: list[dict], memory_items: list[MemoryItem] | None = None) -> tuple[str, dict]:
    ordered_papers = sorted(papers, key=lambda paper: paper["citation_id"])
    memory_items = list(memory_items or [])
    covered_topics = sorted({topic for paper in ordered_papers for topic in paper.get("topic_tags", []) if topic in task_spec.requested_topics})
    source_refs = [paper["citation_id"] for paper in ordered_papers]
    lines = [f"# Literature Review: {task_spec.request_id}", "", f"Variant: `{variant}`", "", "## Scope", ""]
    lines.append(task_spec.normalized_request)
    lines.extend(["", "## Findings by topic", ""])
    if not ordered_papers:
        lines.append("No evidence-backed findings were available.")
    for topic in task_spec.requested_topics:
        topic_papers = [paper for paper in ordered_papers if topic in paper.get("topic_tags", [])]
        if not topic_papers:
            continue
        findings = " ".join(paper["findings"][0] for paper in topic_papers[:2])
        refs = " ".join(f"[{paper['citation_id']}]" for paper in topic_papers[:2])
        lines.append(f"### {topic.replace('_', ' ').title()}")
        lines.append(f"{findings} {refs}".strip())
        lines.append("")
    comparison_done = False
    if task_spec.comparison_mode and len(ordered_papers) >= 2:
        comparison_done = True
        first, second = ordered_papers[0], ordered_papers[-1]
        lines.extend(
            [
                "## Comparison",
                "",
                f"{first['title']} emphasizes {', '.join(first['topic_tags'][:2])}, while {second['title']} emphasizes {', '.join(second['topic_tags'][:2])}. The architecture choice therefore depends on whether the task is bottlenecked by evidence access, retention, or control discipline. [{first['citation_id']}] [{second['citation_id']}]",
                "",
            ]
        )
    recommendation_made = False
    if task_spec.recommendation_required and ordered_papers:
        recommendation_made = True
        lines.extend(
            [
                "## Recommendation",
                "",
                "Prefer the smallest architecture that still keeps goals explicit, evidence grounded, and stop or handoff logic bounded. In this corpus, lightweight planning plus evidence-linked verification is usually the strongest default. "
                + " ".join(f"[{paper['citation_id']}]" for paper in ordered_papers[:2]),
                "",
            ]
        )
    if memory_items:
        lines.extend(["## Memory use", ""])
        for item in memory_items[:2]:
            qualifier = "stale" if item.stale else "fresh"
            lines.append(f"- Used {qualifier} {item.memory_type} memory `{item.entry_id}` tied to {', '.join(item.source_refs) or 'no source refs'}.")
        lines.append("")
    lines.extend(["## Citations", ""])
    for paper in ordered_papers:
        lines.append(f"- [{paper['citation_id']}] {paper['title']} ({paper['year']})")
    metadata = {
        "source_refs": source_refs,
        "covered_topics": covered_topics,
        "comparison_done": comparison_done,
        "recommendation_made": recommendation_made,
        "used_memory_entries": [item.entry_id for item in memory_items],
        "used_stale_memory": any(item.stale for item in memory_items),
    }
    return "\n".join(lines).rstrip() + "\n", metadata
