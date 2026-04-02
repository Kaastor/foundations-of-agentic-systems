# Pokrycie mistrzostwa

Ta tabela mapuje zdolności z slice’ów na konkretne miejsca implementacji, workflowy, testy, dokumenty i obserwowalne artefakty.

| Zdolność | Kod | Workflow | Testy / ewaluacja | Dokumenty | Obserwowalne artefakty |
| --- | --- | --- | --- | --- | --- |
| `AA-C1` rozróżnienie model-agent | `src/m2a/baselines.py`, `src/m2a/control.py` | `m2a run-review`, `m2a compare-architectures` | `tests/test_comparison.py`, `tests/test_stop_and_boundary.py` | `README.md`, `docs/architecture-variants.md`, `docs/slices/AA-S01.md` | `examples/compare_architectures/clear_bounded_review/` |
| `AA-C2` biegłość w pętlach | `src/m2a/state.py`, `src/m2a/control.py` | `m2a run-review` | `tests/test_state_and_traces.py` | `docs/trace-reading.md`, `docs/slices/AA-S03.md` | `trace.jsonl`, `state_snapshots.jsonl` |
| `AA-C3` biegłość w specyfikacji celu | `src/m2a/goals.py` | `m2a spec-review` | `tests/test_goals.py` | `docs/bridge-refresh.md`, `docs/slices/AA-S02.md` | `task_spec.json`, `task_spec.md` |
| `AA-C4` rozumowanie o stanie i pamięci | `src/m2a/state.py`, `src/m2a/memory.py` | `m2a run-review`, `m2a compare-architectures` | `tests/test_state_and_traces.py`, `tests/test_memory.py` | `docs/trace-reading.md`, `docs/slices/AA-S04.md` | `memory_log.jsonl`, `state_snapshots.jsonl`, `examples/run_review/capstone_stale_memory_harms/` |
| `AA-C5` rozumowanie o planowaniu | `src/m2a/planning.py` | `m2a run-review`, `m2a compare-architectures` | `tests/test_planning.py` | `docs/architecture-variants.md`, `docs/slices/AA-S06.md` | `plan.json`, `data/planning/greedy_trap.json` |
| `AA-C6` rozumowanie o działaniach / narzędziach / interfejsach | `src/m2a/tools.py`, `src/m2a/control.py` | `m2a run-review` | `tests/test_tools.py` | `docs/running-case-literature-review-assistant.md`, `docs/slices/AA-S05.md` | `tool_observations.jsonl` |
| `AA-C7` rozumowanie o feedbacku i grounding | `src/m2a/feedback.py`, `src/m2a/synthesis.py` | `m2a run-review`, `m2a compare-architectures` | `tests/test_feedback.py` | `docs/trace-reading.md`, `docs/slices/AA-S07.md` | `verification.jsonl`, `final_review.md`, `failure_diagnosis.md` |
| `AA-C8` zarządzanie granicami | `src/m2a/goals.py`, `src/m2a/control.py` | `m2a spec-review`, `m2a run-review`, `m2a compare-architectures` | `tests/test_stop_and_boundary.py` | `docs/deferred-topics-and-boundaries.md`, `docs/slices/AA-S08.md` | `handoff_note.md`, `boundary_note.md`, `stop_decision.json` |
| `AA-C9` synteza architektoniczna | `src/m2a/comparison.py` | `m2a compare-architectures` | `tests/test_comparison.py` | `docs/capstone-synthesis-guide.md`, `docs/slices/AA-S09.md` | `comparison_matrix.md`, `fit_recommendation.md`, `failure_diagnosis.md` |
