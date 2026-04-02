# Teacher Notes

## Why It Is Here

This assignment targets two common novice errors at once:

- treating memory as generic storage
- treating planning as generic intelligence

## What A Strong Report Should Contain

- a real tradeoff comparison
- concrete before/after evidence from memory and verification artifacts
- the exact bounded intervention in `control.py`
- a short implementation lens pointing to the memory-policy mechanism that changed
- a clear judgment about whether the change improved or harmed bounded behavior

## Common Weak Patterns

- using only generic pros and cons
- describing the code change without showing any observed consequence
- saying the change helped just because it looked more capable
- saying “it depends” without choosing

## Grading Nuance

The strongest answers will usually conclude that loosening stale recall is risky, but full credit does not depend on reaching a predetermined verdict.
What matters is whether the student:

- made the exact bounded change
- compared before and after artifacts honestly
- connected the observed consequence to memory-policy logic
