from pathlib import Path

from m2a.control import run_variant
from m2a.goals import build_task_spec

DATA = Path(__file__).resolve().parents[1] / "data"


def test_boundary_request_results_in_explicit_handoff(tmp_path) -> None:
    request = (DATA / "requests" / "boundary_handoff.txt").read_text(encoding="utf-8")
    spec = build_task_spec(request, request_id="boundary_handoff")
    result = run_variant(spec, "capstone_agent", tmp_path / "boundary")
    assert result.stop_decision.outcome == "handoff"
    assert result.handoff_note is not None
    assert spec.boundary_topics


def test_ambiguous_request_results_in_clarification(tmp_path) -> None:
    request = (DATA / "requests" / "ambiguous_request.txt").read_text(encoding="utf-8")
    spec = build_task_spec(request, request_id="ambiguous_request")
    result = run_variant(spec, "capstone_agent", tmp_path / "ambiguous")
    assert result.stop_decision.outcome == "clarification_needed"
    assert result.handoff_note is not None


def test_blocking_verification_prevents_successful_stop(tmp_path) -> None:
    request = (DATA / "requests" / "clear_bounded_review.txt").read_text(encoding="utf-8")
    spec = build_task_spec(request, request_id="clear_bounded_review")
    result = run_variant(spec, "model_only", tmp_path / "model-only")
    assert result.stop_decision.outcome != "success"
