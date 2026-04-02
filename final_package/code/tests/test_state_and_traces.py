from pathlib import Path

from m2a.control import run_variant
from m2a.goals import build_task_spec

DATA = Path(__file__).resolve().parents[1] / "data"


def test_trace_contains_loop_phases_and_state_is_separated(tmp_path) -> None:
    request = (DATA / "requests" / "clear_bounded_review.txt").read_text(encoding="utf-8")
    spec = build_task_spec(request, request_id="clear_bounded_review")
    result = run_variant(spec, "capstone_agent", tmp_path / "run")
    phases = {event.phase for event in result.trace}
    assert {"observe", "think", "act", "verify"} <= phases
    snapshot = result.state_snapshots[-1]
    assert "recent_observation_refs" in snapshot.active_context
    assert "read_papers" in snapshot.external_state
    assert "policy" in snapshot.memory_summary
