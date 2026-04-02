from m2a.memory import MemoryPolicy, MemoryStore, load_seed_memory


def test_memory_retrieval_excludes_stale_by_default() -> None:
    store = MemoryStore(MemoryPolicy("test", max_entries=10, retrieval_limit=5, stale_after_steps=10, allow_writes=True, allow_stale_recall=False), load_seed_memory())
    items = store.retrieve(["reflection"], step=1)
    assert all(not item.stale for item in items)


def test_memory_forget_policy_eviction_when_over_capacity() -> None:
    store = MemoryStore(MemoryPolicy("tiny", max_entries=1, retrieval_limit=1, stale_after_steps=10, allow_writes=True))
    store.write("note", "first", ["P04-MemoryPolicy"], ["memory"], step=1)
    store.write("note", "second", ["P06-PlanSketch"], ["planning"], step=2)
    assert len(store.items) == 1
    assert any(event.event_type == "forget" for event in store.events)


def test_memory_retrieval_limit_prevents_over_retrieval() -> None:
    store = MemoryStore(MemoryPolicy("limit", max_entries=10, retrieval_limit=1, stale_after_steps=10, allow_writes=True), load_seed_memory())
    items = store.retrieve(["memory", "planning", "grounding"], step=1)
    assert len(items) == 1
