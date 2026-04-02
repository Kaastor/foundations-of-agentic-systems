import json
from pathlib import Path

from m2a.planning import missing_topics_from_verification, needs_replan, select_papers
from m2a.schemas import VerificationResult

DATA = Path(__file__).resolve().parents[1] / "data"


def test_coverage_selection_beats_greedy_on_branching_fixture() -> None:
    fixture = json.loads((DATA / "planning" / "greedy_trap.json").read_text(encoding="utf-8"))
    greedy = select_papers(fixture["results"], fixture["requested_topics"], fixture["budget"], strategy="greedy")
    coverage = select_papers(fixture["results"], fixture["requested_topics"], fixture["budget"], strategy="coverage")
    greedy_topics = {topic for item in greedy for topic in item["topic_tags"]}
    coverage_topics = {topic for item in coverage for topic in item["topic_tags"]}
    assert len(coverage_topics & set(fixture["requested_topics"])) > len(greedy_topics & set(fixture["requested_topics"]))


def test_replan_trigger_detects_missing_topics() -> None:
    verification = VerificationResult(
        step=1,
        stage="intermediate",
        satisfied=False,
        checks={},
        blocking_issues=["planning: missing topic coverage for grounding, memory"],
        non_blocking_issues=[],
        evidence_refs=["P06-PlanSketch"],
    )
    assert needs_replan(verification)
    assert missing_topics_from_verification(verification) == ["grounding", "memory"]
