# Shared Submission Rules

## If You Remember Only Five Things

- submit one file: `submission.md`
- follow the assignment-specific report template
- AI use is allowed
- evidence matters more than polish
- every assignment includes one implementation lens, and Assignments 5-6 also require a bounded code change with before/after comparison

## Submission Mode

All assignments are `report_only`.

Submit one Markdown report per assignment.
The canonical filename is:

- `submission.md`

PDF export is acceptable only if required by the course platform, but Markdown is the source of truth.

## Time Expectation

Default expected time per assignment:

- `4 hours`

You do not need to use the whole time.
You do need to use the time to gather enough evidence for a defensible report.

## Allowed AI Use

Allowed and normal:

- chatbots
- AI drafting help
- AI summarization
- optional coding-agent help
- bounded manual code edits in assignments that explicitly require them

Not required:

- premium coding-agent access
- proprietary tools
- code generation beyond what is needed to inspect, rerun, or make one bounded course-specified change in the provided package

The assignments are designed so that a student using only normal chatbots can still finish successfully.

## What You Are Graded On

You are not graded for hiding AI use.
You are graded for:

- understanding the task correctly
- using evidence from course artifacts or readings
- using one bounded implementation lens from the shipped source code
- comparing plausible options rather than accepting the first answer
- critiquing unsupported or weak claims
- making a bounded revision or defended selection
- justifying your final judgment clearly

## Required Report Structure

Every assignment-specific template is a local version of the same structure:

1. `Task`
2. `Candidate Options Or Initial Answer`
3. `Comparison Criteria`
4. `Evidence`
5. `Implementation Lens`
6. `Critique`
7. `Revision Or Selected Option`
8. `Final Justification`
9. `Uncertainty Or Remaining Weakness`

Follow the local template in the assignment folder, but do not remove these core sections.

## Evidence Rules

Your report must cite concrete evidence.

Good evidence includes:

- exact file paths from the course package
- exact artifact names
- exact fields, steps, variants, or observations
- one exact source module or function boundary when the assignment asks for an implementation lens
- short quoted snippets when necessary
- comparison of two explicit alternatives

Weak evidence includes:

- broad paraphrases with no artifact reference
- “the AI said”
- “it seems”
- generic course concepts with no link to the assignment materials

## Citation Style

When citing course artifacts, use:

- file path
- artifact name
- optional field, section, step, or event identifier

Example:

- `code/examples/compare_architectures/clear_bounded_review/comparison_matrix.md`
- `code/examples/run_review/capstone_ambiguous_request/trace.jsonl`, step 4
- `code/examples/spec_review/ambiguous_request/task_spec.json`, stop conditions

## AI Use Disclosure

You do not need to disclose every prompt you used.
You do need to make clear:

- what candidate options or initial answer you started from
- what you kept
- what you rejected
- what you revised

If AI helped produce an initial answer, include the relevant claims inside the report instead of hiding them.

## Implementation Lens Rule

Every assignment includes one small required implementation lens.

This means:

- inspect one relevant source module, function boundary, or implementation surface named in `code_context.md`
- explain in a few sentences how that implementation choice helps produce, constrain, or explain the observed artifact or behavior
- keep this section short and bounded

The implementation lens itself is not a coding assignment.
In Assignments 1-4, you are not required to edit code.
The purpose is to connect concept, artifact, and implementation.

## Code-Change Rule For Later Assignments

Assignments 5 and 6 require one bounded code change in your own working copy of the course repository.

For those assignments, your report must also include:

- the exact file changed
- the exact bounded intervention you made
- your predicted effect before rerunning
- before and after artifact evidence
- a judgment about whether the change improved, harmed, or only weakly changed the bounded behavior

You still submit only `submission.md`.
You do not submit a separate code artifact unless the teacher asks for it later.

## Operational Rule

Do not submit a polished conclusion with weak evidence.

If forced to choose, prefer:

- a narrower, well-supported answer

over:

- a broader, more confident answer with weak support
