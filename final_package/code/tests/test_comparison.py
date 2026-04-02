from pathlib import Path

from m2a.artifacts import load_task_spec
from m2a.cli import main

DATA = Path(__file__).resolve().parents[1] / "data"


def test_variants_produce_structurally_different_outputs(tmp_path) -> None:
    request_file = DATA / "requests" / "clear_bounded_review.txt"
    spec_dir = tmp_path / "spec"
    compare_dir = tmp_path / "compare"
    main(["spec-review", str(request_file), "--out-dir", str(spec_dir)])
    task_spec = spec_dir / "task_spec.json"
    main(["compare-architectures", str(task_spec), "--out-dir", str(compare_dir)])

    model_summary = load_task_spec(task_spec)  # smoke check load path
    assert model_summary.request_id == "clear_bounded_review"

    model_trace = (compare_dir / "variants" / "model_only" / "trace.jsonl").read_text(encoding="utf-8")
    capstone_trace = (compare_dir / "variants" / "capstone_agent" / "trace.jsonl").read_text(encoding="utf-8")
    assert model_trace != capstone_trace
    capstone_summary = (compare_dir / "variants" / "capstone_agent" / "run_summary.json").read_text(encoding="utf-8")
    assert "reflection_actions" in capstone_summary


def test_small_task_can_recommend_scripted_pipeline(tmp_path) -> None:
    request_file = DATA / "requests" / "over_planning_overhead.txt"
    spec_dir = tmp_path / "spec"
    compare_dir = tmp_path / "compare"
    main(["spec-review", str(request_file), "--out-dir", str(spec_dir)])
    task_spec = spec_dir / "task_spec.json"
    main(["compare-architectures", str(task_spec), "--out-dir", str(compare_dir)])
    recommendation = (compare_dir / "fit_recommendation.md").read_text(encoding="utf-8")
    assert "scripted_pipeline" in recommendation
