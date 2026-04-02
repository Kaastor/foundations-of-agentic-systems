from pathlib import Path

from m2a.cli import main

DATA = Path(__file__).resolve().parents[1] / "data"


def test_cli_spec_run_and_compare(tmp_path) -> None:
    request_file = DATA / "requests" / "clear_bounded_review.txt"
    spec_dir = tmp_path / "spec"
    run_dir = tmp_path / "run"
    compare_dir = tmp_path / "compare"

    assert main(["spec-review", str(request_file), "--out-dir", str(spec_dir)]) == 0
    task_spec_file = spec_dir / "task_spec.json"
    assert task_spec_file.exists()

    assert main(["run-review", str(task_spec_file), "--variant", "capstone_agent", "--out-dir", str(run_dir)]) == 0
    assert (run_dir / "plan.json").exists()
    assert (run_dir / "trace.jsonl").exists()
    assert (run_dir / "stop_decision.json").exists()

    assert main(["compare-architectures", str(task_spec_file), "--out-dir", str(compare_dir)]) == 0
    assert (compare_dir / "comparison_matrix.md").exists()
    assert (compare_dir / "fit_recommendation.md").exists()
    assert (compare_dir / "variants" / "capstone_agent" / "trace.jsonl").exists()
