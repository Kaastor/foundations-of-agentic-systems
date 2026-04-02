# Teacher Notes

## Why It Is Here

This is the capstone assignment for the six-meeting spine.

## What A Strong Report Should Contain

- separate treatment of the in-scope and boundary cases
- a real before/after comparison of the boundary recommendation
- the exact bounded intervention in `comparison.py`
- a short implementation lens showing why explicit boundary handling exists in the recommendation layer
- recognition that `boundary_note.md` may remain unchanged because the repository boundary still exists even when the recommendation layer is stressed
- explicit stop or handoff logic
- bounded final recommendations rather than “best overall” slogans

## Common Weak Patterns

- choosing one architecture as universally best
- discussing reflection or verification abstractly with no artifact use
- accepting the stressed recommendation as better just because it names a concrete variant
- ignoring the difference between recommendation output and repository boundary logic

## Grading Nuance

This is the most synthetic assignment.
Allow some stylistic variation, but require strict boundedness and real evidence use.
The strongest answers will usually reject the stress-test patch, but full credit depends on honest before/after reasoning rather than on a predetermined slogan.
