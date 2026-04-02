from m2a.feedback import reflection_actions
from m2a.schemas import VerificationResult


def test_reflection_requires_evidence_or_blocking_issue() -> None:
    clear = VerificationResult(step=1, stage="intermediate", satisfied=True, checks={}, blocking_issues=[], non_blocking_issues=[], evidence_refs=[])
    assert reflection_actions(clear, critique="maybe do better") == []

    blocked = VerificationResult(
        step=2,
        stage="intermediate",
        satisfied=False,
        checks={},
        blocking_issues=["planning: missing topic coverage for grounding"],
        non_blocking_issues=[],
        evidence_refs=["P10-ToolRichNoMemory"],
    )
    assert reflection_actions(blocked) == ["search:grounding"]
