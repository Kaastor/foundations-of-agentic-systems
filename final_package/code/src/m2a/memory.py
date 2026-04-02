from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

from .schemas import MemoryItem, MemoryLogEvent

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MEMORY_PATH = REPO_ROOT / "data" / "memory" / "seed_memory.jsonl"


@dataclass(frozen=True, slots=True)
class MemoryPolicy:
    name: str
    max_entries: int
    retrieval_limit: int
    stale_after_steps: int
    allow_writes: bool
    allow_stale_recall: bool = False


def load_seed_memory(path: str | Path = DEFAULT_MEMORY_PATH) -> list[MemoryItem]:
    entries: list[MemoryItem] = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.strip():
            entries.append(MemoryItem.from_dict(json.loads(line)))
    return entries


class MemoryStore:
    def __init__(self, policy: MemoryPolicy, initial_items: Iterable[MemoryItem] | None = None) -> None:
        self.policy = policy
        self.items: list[MemoryItem] = []
        self.events: list[MemoryLogEvent] = [
            MemoryLogEvent(
                step=0,
                event_type="policy_snapshot",
                entry_id=policy.name,
                memory_type="policy",
                content=f"Memory policy {policy.name}",
                source_refs=[],
                tags=[],
                policy_reason="Initial memory policy.",
                policy=asdict(policy),
            )
        ]
        if initial_items:
            self.seed(initial_items)

    def seed(self, items: Iterable[MemoryItem]) -> None:
        for item in items:
            self.items.append(item)
            self.events.append(
                MemoryLogEvent(
                    step=item.created_step,
                    event_type="seed",
                    entry_id=item.entry_id,
                    memory_type=item.memory_type,
                    content=item.content,
                    source_refs=list(item.source_refs),
                    tags=list(item.tags),
                    policy_reason="Seeded memory loaded for this run.",
                    stale=item.stale,
                )
            )
        self._enforce_capacity(step=0)

    def write(self, memory_type: str, content: str, source_refs: list[str], tags: list[str], step: int) -> MemoryItem | None:
        if not self.policy.allow_writes:
            self.events.append(
                MemoryLogEvent(
                    step=step,
                    event_type="write_blocked",
                    entry_id=f"blocked-{step}",
                    memory_type=memory_type,
                    content=content,
                    source_refs=list(source_refs),
                    tags=list(tags),
                    policy_reason="Writes are disabled by this memory policy.",
                )
            )
            return None
        item = MemoryItem(
            entry_id=f"{memory_type}-{step}-{len(self.items)+1}",
            memory_type=memory_type,
            content=content,
            source_refs=list(source_refs),
            tags=list(tags),
            created_step=step,
            stale=False,
        )
        self.items.append(item)
        self.events.append(
            MemoryLogEvent(
                step=step,
                event_type="write",
                entry_id=item.entry_id,
                memory_type=item.memory_type,
                content=item.content,
                source_refs=item.source_refs,
                tags=item.tags,
                policy_reason="Stored new evidence-linked memory.",
                stale=item.stale,
            )
        )
        self._mark_stale(step)
        self._enforce_capacity(step)
        return item

    def retrieve(self, query_terms: list[str], step: int) -> list[MemoryItem]:
        lowered_terms = {term.lower() for term in query_terms if term}
        scored: list[tuple[int, MemoryItem]] = []
        for item in self.items:
            haystack = " ".join([item.content, *item.tags, *item.source_refs]).lower()
            score = sum(1 for term in lowered_terms if term in haystack)
            if score == 0:
                continue
            if item.stale and not self.policy.allow_stale_recall:
                continue
            scored.append((score, item))
        scored.sort(key=lambda pair: (-pair[0], pair[1].entry_id))
        selected = [item for _, item in scored[: self.policy.retrieval_limit]]
        for item in selected:
            self.events.append(
                MemoryLogEvent(
                    step=step,
                    event_type="retrieve",
                    entry_id=item.entry_id,
                    memory_type=item.memory_type,
                    content=item.content,
                    source_refs=item.source_refs,
                    tags=item.tags,
                    policy_reason="Retrieved because query terms overlapped with stored content or tags.",
                    stale=item.stale,
                )
            )
        return selected

    def diagnostics(self) -> dict[str, object]:
        return {
            "policy": asdict(self.policy),
            "stored_entries": len(self.items),
            "stale_entries": [item.entry_id for item in self.items if item.stale],
            "memory_types": sorted({item.memory_type for item in self.items}),
        }

    def _mark_stale(self, step: int) -> None:
        if self.policy.stale_after_steps <= 0:
            return
        for item in self.items:
            if step - item.created_step >= self.policy.stale_after_steps:
                item.stale = True

    def _enforce_capacity(self, step: int) -> None:
        while len(self.items) > self.policy.max_entries:
            removed = self.items.pop(0)
            self.events.append(
                MemoryLogEvent(
                    step=step,
                    event_type="forget",
                    entry_id=removed.entry_id,
                    memory_type=removed.memory_type,
                    content=removed.content,
                    source_refs=removed.source_refs,
                    tags=removed.tags,
                    policy_reason="Forgot the oldest entry to maintain bounded memory size.",
                    stale=removed.stale,
                )
            )
