from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .artifacts import emit_run_artifacts, emit_task_spec, load_task_spec
from .comparison import compare_architectures
from .control import VALID_VARIANTS, run_variant
from .goals import build_task_spec, read_request_input


def _default_out_dir(command: str, name: str) -> Path:
    return Path("scratch") / command / name


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="m2a", description="Model-to-agent checkpoint CLI.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    spec = subparsers.add_parser("spec-review", help="Transform a request into a structured task spec.")
    spec.add_argument("request_input", help="Path to a request fixture or a plain-text request.")
    spec.add_argument("--out-dir", default=None, help="Output directory for task_spec artifacts.")

    run = subparsers.add_parser("run-review", help="Run one architecture variant on a task spec.")
    run.add_argument("task_spec_file", help="Path to task_spec.json.")
    run.add_argument("--variant", required=True, choices=VALID_VARIANTS)
    run.add_argument("--out-dir", default=None, help="Output directory for run artifacts.")

    compare = subparsers.add_parser("compare-architectures", help="Run multiple variants on the same task spec.")
    compare.add_argument("task_spec_file", help="Path to task_spec.json.")
    compare.add_argument("--variants", nargs="+", default=None, choices=VALID_VARIANTS)
    compare.add_argument("--out-dir", default=None, help="Output directory for comparison artifacts.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "spec-review":
            request_text, request_id = read_request_input(args.request_input)
            spec = build_task_spec(request_text, request_id=request_id)
            out_dir = Path(args.out_dir) if args.out_dir else _default_out_dir("spec-review", spec.request_id)
            emit_task_spec(spec, out_dir)
            print(out_dir)
            return 0

        if args.command == "run-review":
            spec = load_task_spec(args.task_spec_file)
            out_dir = Path(args.out_dir) if args.out_dir else _default_out_dir("run-review", f"{spec.request_id}-{args.variant}")
            result = run_variant(spec, args.variant, out_dir)
            emit_run_artifacts(result, out_dir)
            print(out_dir)
            return 0

        if args.command == "compare-architectures":
            spec = load_task_spec(args.task_spec_file)
            out_dir = Path(args.out_dir) if args.out_dir else _default_out_dir("compare-architectures", spec.request_id)
            compare_architectures(spec, out_dir, args.variants)
            print(out_dir)
            return 0
    except (FileNotFoundError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
