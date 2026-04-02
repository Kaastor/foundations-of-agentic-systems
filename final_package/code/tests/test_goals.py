from pathlib import Path

from m2a.artifacts import read_json
from m2a.goals import build_task_spec

DATA = Path(__file__).resolve().parents[1] / "data"


def test_build_task_spec_matches_expected_clear() -> None:
    request = (DATA / "requests" / "clear_bounded_review.txt").read_text(encoding="utf-8")
    spec = build_task_spec(request, request_id="clear_bounded_review")
    expected = read_json(DATA / "expected_task_specs" / "clear_bounded_review.json")
    assert spec.to_dict() == expected


def test_ambiguity_detection_for_ambiguous_request() -> None:
    request = (DATA / "requests" / "ambiguous_request.txt").read_text(encoding="utf-8")
    spec = build_task_spec(request, request_id="ambiguous_request")
    assert spec.ambiguity_flags
    assert spec.clarification_questions
    assert not spec.requested_topics
