# Foundations of Agent Architectures: From Generative Models to Goal-Directed Systems

## Course Overview

This package provides an understanding-first introduction to a specific and important area within generative AI: the architectural transition from a generative model to a bounded, goal-directed agentic system.

It is not intended as a general introduction to all of GenAI. Its focus is narrower and more precise. The package is organized around the study of agent architectures: explicit goals, control loops, state, memory, planning, tool use, verification, stopping conditions, handoff logic, and comparative architectural judgment.

The central question of the course is:

> How does a generative model become a bounded, goal-directed agentic system through architecture?

## Start Here

If you are a student, begin in this order:

1. [STUDENT_SETUP.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/STUDENT_SETUP.md)
2. [assignments/README.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/assignments/README.md)
3. [book.pdf](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/book/book.pdf)
   Chapter 1, pages 7-15

If you are the teacher, begin in this order:

1. [lesson_0.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/assignments/lesson_0.md)
2. [TEACHER_GUIDE.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/TEACHER_GUIDE.md)
3. [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/meeting_plan.md)
4. [meeting_prep_checklist.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/meeting_prep_checklist.md)

## Document Roles

Use the package documents with a clear division of labor:

- [README.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/README.md): what the course is, why it exists, and how the package is structured
- [STUDENT_SETUP.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/STUDENT_SETUP.md): local setup and runnable workflow only
- [assignments/README.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/assignments/README.md): how assignments work and how the assignment folders are organized
- [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/meeting_plan.md): the course spine and per-meeting learning structure
- [TEACHER_GUIDE.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/TEACHER_GUIDE.md): teacher operating model and pre-course threshold
- [lesson_0.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/assignments/lesson_0.md): shared `Lesson 0` knowledge file, with conceptual content plus local course-instance fields

## Intended Audience

This course is designed for:

- students seeking a rigorous conceptual foundation before specialization
- self-directed learners who want structural understanding rather than framework recipes
- engineers and technical readers who need a clear account of how agentic systems are composed
- early-stage researchers who want a bounded, inspectable entry point into agent architecture

The course assumes comfort with abstraction, stepwise reasoning, and basic computational thinking. Prior experience with reinforcement learning, information retrieval, symbolic planning, or production systems is not required. Basic programming familiarity is helpful, but not essential for the conceptual portions of the package.

## Educational Aim

The aim of this package is to develop structural literacy about agentic systems. Students should finish the course able to analyze an unfamiliar system in terms of its task representation, control structure, state management, memory policy, tool interfaces, verification logic, and stopping or handoff conditions.

The package therefore emphasizes:

- explicit architectural distinctions rather than vague agent terminology
- inspectable traces and artifacts rather than opaque demonstrations
- deterministic, offline workflows rather than hidden model behavior
- bounded reasoning about system design rather than broad claims about GenAI as a whole

## Learning Outcomes

By the end of the course, a student should be able to:

- explain the distinction between a model-only response, a scripted workflow, and an agentic loop
- convert a vague request into an explicit task specification with constraints, success criteria, and stopping conditions
- distinguish context, external state, persistent memory, observations, and execution traces
- explain memory as representation plus policy rather than as generic storage
- analyze tool use as a contract with the environment rather than as a cosmetic extension
- reason about planning, decomposition, replanning, and action selection in bounded settings
- connect verification and feedback to downstream control decisions
- treat clarification, stopping, and handoff as components of correctness
- compare alternative architectures on the same task and justify which one is the better fit

## Running Case

The package is anchored in one bounded application: an offline literature-review assistant.

This case is intentionally constrained. It is large enough to expose the deep core of agent architecture, yet small enough to remain deterministic, inspectable, and pedagogically tractable. The aim is not to build a production research assistant, but to make architectural structure visible.

## Scope and Deliberate Exclusions

This course is not primarily about:

- vendor APIs or framework-specific orchestration
- prompt engineering as a collection of heuristics
- live web retrieval or production RAG systems
- retrieval internals or ranking algorithms
- reinforcement-learning-based control
- formal symbolic planning frameworks
- deployment, observability, governance, or production operations

These areas are important, but they are adjacent domains rather than the instructional focus of this package.

## Why This Is a Useful Foundation

This course serves as a strong foundation for several later study and practice paths. In particular, it prepares students for:

- further study in agent engineering, especially where explicit goals, tools, memory, and verification must be coordinated
- more advanced work on reliable tool-using systems, including grounded assistants and retrieval-augmented workflows
- subsequent courses in planning, sequential decision-making, or reinforcement learning, where control structure becomes more formal
- study of evaluation and reliability in GenAI systems, especially where process and outcome must be distinguished
- work in human-agent interaction, mixed-initiative systems, and delegation design
- research or engineering paths concerned with memory, representation, world models, and long-horizon system behavior

Its value as a foundation lies in the fact that it teaches the architectural vocabulary and conceptual distinctions that recur across many subfields of modern GenAI systems work.

## Package Structure

The package contains two complementary components:

- `book/` contains the conceptual reading material
- `code/` contains the deterministic teaching repository in which the conceptual material becomes concrete

It also includes the course-delivery layer:

- [meeting_plan.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/meeting_plan.md) for the six-meeting backbone
- [TEACHER_GUIDE.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/TEACHER_GUIDE.md) for teacher preparation
- [meeting_prep_checklist.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/meeting_prep_checklist.md) for meeting-by-meeting execution
- [STUDENT_SETUP.md](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/STUDENT_SETUP.md) for student runtime and local workflow setup
- [assignments](/home/przemek/Biznes/Kursy/course-generation/understanding/runs/Agentic-GenAI-Systems/final_package/assignments) for reports, grading rules, and Lesson 0 onboarding

Within `code/`, students will find:

- `src/` for the implementation
- `docs/` for repository-specific explanations and slice guides
- `examples/` for committed reference artifacts
- `data/` for local fixtures and the synthetic corpus
- `tests/` for behavior checks and regression coverage

## Distinctive Features of the Package

This package is organized around several explicit teaching commitments:

- deterministic behavior instead of hidden external model calls
- inspectable outputs instead of impressionistic demos
- bounded scope instead of an undifferentiated introduction to all of GenAI
- architecture comparison instead of one-pattern advocacy
- transferable conceptual understanding instead of vendor-specific tool training

## Expected Outcome

Students who complete this package should acquire more than familiarity with agent terminology. They should be able to reconstruct the architecture of an unfamiliar system, explain why it behaves as it does, identify likely structural failure points, and reason about when one architecture is more appropriate than another.

The primary educational outcome is therefore structural literacy about agentic systems.
