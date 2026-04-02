# AI Use Guidance

## Chatbots

Useful for:

- generating an initial recommendation set
- predicting what disabling the boundary branch in `_render_recommendation()` might do

## Coding Agents

Optional only.
Useful for:

- locating the exact condition to edit inside `_render_recommendation()`
- diffing the before and after recommendation files quickly

## Weak AI Use

- making the stress-test patch and then trusting the changed recommendation without critiquing it

## Strong AI Use

- generating a prediction before the stress test
- using AI to help make the bounded edit
- comparing before and after recommendation artifacts
- being willing to conclude that the stressed recommendation is worse than the original bounded rule
