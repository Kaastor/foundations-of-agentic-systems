# Meeting Plan

## Six Meetings

### Meeting 1. What Makes a System Agentic?

**Technical subtitle:** From Model to Agent

**Core question:** What has to be added around a generative model before it is reasonable to call the whole system agentic?

**Why this meeting comes first:** Students need a stable distinction among model-only behavior, scripted workflows, and adaptive agentic loops before any later discussion of state, tools, memory, or planning makes sense.

**Reading focus:**
- model vs interactive vs scripted vs agentic
- minimal control loop
- agency as an architectural property

**Book supplementary material:**
- Primary reading: `book/book.pdf`, Chapter 1, pages 7-15
- Focus inside the reading: the model/scripted/agentic distinction, the minimal loop, and the running literature-review request

**Repo support:**
- Overview and framing: `code/README.md`
- Supporting docs: `code/docs/architecture-variants.md`, `code/docs/running-case-literature-review-assistant.md`, `code/docs/slices/AA-S01.md`
- Reference artifacts: `code/examples/compare_architectures/clear_bounded_review/`
- Code and tests: `code/src/m2a/baselines.py`, `code/src/m2a/control.py`, `code/tests/test_comparison.py`
- Suggested workflow: `poetry run m2a compare-architectures data/expected_task_specs/clear_bounded_review.json --out-dir scratch/compare-clear`

**Running case focus:** Compare prompt-only, scripted, and loop-based versions of the literature-review assistant.

### Meeting 2. What Exactly Is the Task?

**Technical subtitle:** Task Specification: Goals, Constraints, Success, Stop

**Core question:** How does a raw user request become an explicit task contract that can steer system behavior?

**Why this meeting comes second:** Once students know what kind of system they are studying, they need to know what that system is actually trying to satisfy.

**Reading focus:**
- user request vs task specification
- goals, constraints, success criteria
- stop and handoff conditions
- clarification as a legitimate design move

**Book supplementary material:**
- Primary reading: `book/book.pdf`, Chapter 2, pages 16-23
- Focus inside the reading: request vs task specification, ambiguity handling, and stop or handoff conditions

**Repo support:**
- Supporting docs: `code/docs/slices/AA-S02.md`
- Request fixtures: `code/data/requests/clear_bounded_review.txt`, `code/data/requests/ambiguous_request.txt`, `code/data/requests/boundary_handoff.txt`
- Reference artifacts: `code/examples/spec_review/clear_bounded_review/`, `code/examples/spec_review/ambiguous_request/`, `code/examples/spec_review/boundary_handoff/`
- Code and tests: `code/src/m2a/goals.py`, `code/src/m2a/artifacts.py`, `code/tests/test_goals.py`
- Suggested workflows:
  - `poetry run m2a spec-review data/requests/clear_bounded_review.txt --out-dir scratch/spec-clear`
  - `poetry run m2a spec-review data/requests/ambiguous_request.txt --out-dir scratch/spec-ambiguous`

**Running case focus:** Rewrite vague literature-review requests into bounded task specifications.

### Meeting 3. What Does the System Carry Across Steps?

**Technical subtitle:** Control Loops, State, Context, and Traces

**Core question:** What information persists, what changes, and what disappears as the system runs?

**Why this meeting comes third:** Students cannot reason about agent behavior unless they can trace where information lives and how it moves across steps.

**Reading focus:**
- control loops over time
- context vs external state vs world state
- execution traces
- plan vs trace

**Book supplementary material:**
- Primary reading: `book/book.pdf`, Chapter 3, pages 24-31
- Optional preview: `book/book.pdf`, Chapter 4, pages 32-35 if students need an early bridge into persistence

**Repo support:**
- Supporting docs: `code/docs/trace-reading.md`, `code/docs/slices/AA-S03.md`
- Reference artifacts:
  - `code/examples/compare_architectures/clear_bounded_review/variants/capstone_agent/trace.jsonl`
  - `code/examples/compare_architectures/clear_bounded_review/variants/capstone_agent/state_snapshots.jsonl`
  - `code/examples/run_review/capstone_ambiguous_request/trace.jsonl`
- Code and tests: `code/src/m2a/state.py`, `code/src/m2a/control.py`, `code/tests/test_state_and_traces.py`
- Suggested workflow: `poetry run m2a run-review data/expected_task_specs/clear_bounded_review.json --variant capstone_agent --out-dir scratch/run-clear`

**Running case focus:** Read a multi-step literature-review run and identify where an error first became visible.

### Meeting 4. How Does It Act and What Counts as Evidence?

**Technical subtitle:** Action Selection, Tools, and Grounding

**Core question:** How does the system choose among thinking, asking, acting, and stopping, and what observations count as grounded evidence?

**Why this meeting comes fourth:** After students can trace the loop, they are ready to understand how the loop actually couples to tools and environment.

**Reading focus:**
- think / ask / act / stop
- tool contracts
- side effects
- grounded vs ungrounded outputs

**Book supplementary material:**
- Primary reading: `book/book.pdf`, Chapter 5, pages 42-49
- Focus inside the reading: action choice, tool contracts, observation channels, and grounded evidence

**Repo support:**
- Supporting docs: `code/docs/architecture.md`, `code/docs/running-case-literature-review-assistant.md`, `code/docs/slices/AA-S05.md`
- Reference artifacts:
  - `code/examples/compare_architectures/clear_bounded_review/variants/capstone_agent/tool_observations.jsonl`
  - `code/examples/compare_architectures/clear_bounded_review/variants/scripted_pipeline/tool_observations.jsonl`
- Code and tests: `code/src/m2a/tools.py`, `code/src/m2a/control.py`, `code/tests/test_tools.py`
- Suggested workflow: `poetry run m2a run-review data/expected_task_specs/clear_bounded_review.json --variant capstone_agent --out-dir scratch/run-tools`

**Running case focus:** Define the assistant's search, reading, note, and citation-check interactions as explicit tool contracts.

### Meeting 5. What Should Persist and When Should It Plan?

**Technical subtitle:** Memory, Planning, and Replanning

**Core question:** What information should the system persist, and when does explicit planning help rather than hurt?

**Why this meeting comes fifth:** Memory and planning become meaningful only after students understand tasks, state, traces, and action interfaces.

**Reading focus:**
- memory types and policies
- persistence tradeoffs
- decomposition and replanning
- memory-rich vs tool-rich tradeoffs

**Book supplementary material:**
- Primary reading: `book/book.pdf`, Chapter 4, pages 32-41
- Supplementary reading: `book/book.pdf`, Chapter 6, pages 50-58
- Focus inside the reading: memory as policy, decomposition, replanning, and the cost of over-planning

**Repo support:**
- Supporting docs: `code/docs/slices/AA-S04.md`, `code/docs/slices/AA-S06.md`
- Supporting data and artifacts:
  - `code/data/memory/seed_memory.jsonl`
  - `code/data/planning/greedy_trap.json`
  - `code/data/expected_task_specs/stale_memory_harms.json`
  - `code/data/expected_task_specs/tradeoff_memory_vs_tools.json`
  - `code/examples/run_review/capstone_stale_memory_harms/memory_log.jsonl`
  - `code/examples/run_review/capstone_stale_memory_harms/plan.json`
- Code and tests: `code/src/m2a/memory.py`, `code/src/m2a/planning.py`, `code/tests/test_memory.py`, `code/tests/test_planning.py`
- Suggested workflows:
  - `poetry run m2a run-review data/expected_task_specs/stale_memory_harms.json --variant capstone_agent --out-dir scratch/run-memory`
  - `poetry run m2a compare-architectures data/expected_task_specs/tradeoff_memory_vs_tools.json --out-dir scratch/compare-tradeoff`

**Running case focus:** Compare a memory-rich and a tool-rich literature-review assistant, then justify a minimal planning structure.

### Meeting 6. How Does It Stay Bounded and How Do We Compare Designs?

**Technical subtitle:** Feedback, Verification, Stopping, Handoff, and Architecture Synthesis

**Core question:** How does the system know whether to continue, revise, stop, hand off, or recommend a different architecture entirely?

**Why this meeting comes last:** This meeting depends on everything before it: goals, traces, tools, memory, planning, and grounded evidence.

**Reading focus:**
- verification and feedback
- reflection tied to evidence
- stopping and handoff
- architecture comparison by task shape

**Book supplementary material:**
- Primary reading: `book/book.pdf`, Chapter 7, pages 59-66; Chapter 8, pages 67-77; Chapter 9, pages 78-85
- Capstone follow-up: `book/book.pdf`, Chapter 10, pages 86-98
- Focus inside the reading: verification, bounded autonomy, architecture fit, and defended synthesis

**Repo support:**
- Supporting docs:
  - `code/docs/slices/AA-S07.md`
  - `code/docs/slices/AA-S08.md`
  - `code/docs/slices/AA-S09.md`
  - `code/docs/capstone-synthesis-guide.md`
  - `code/docs/misconceptions-and-failure-modes.md`
  - `code/docs/deferred-topics-and-boundaries.md`
- Reference artifacts:
  - `code/examples/run_review/capstone_ambiguous_request/verification.jsonl`
  - `code/examples/run_review/capstone_ambiguous_request/handoff_note.md`
  - `code/examples/compare_architectures/clear_bounded_review/`
  - `code/examples/compare_architectures/boundary_handoff/`
- Code and tests: `code/src/m2a/feedback.py`, `code/src/m2a/comparison.py`, `code/src/m2a/synthesis.py`, `code/tests/test_feedback.py`, `code/tests/test_stop_and_boundary.py`, `code/tests/test_comparison.py`
- Suggested workflows:
  - `poetry run m2a compare-architectures data/expected_task_specs/clear_bounded_review.json --out-dir scratch/compare-clear`
  - `poetry run m2a compare-architectures data/expected_task_specs/boundary_handoff.json --out-dir scratch/compare-boundary`

**Running case focus:** Diagnose failures, compare variants, and defend a bounded literature-review assistant architecture.
