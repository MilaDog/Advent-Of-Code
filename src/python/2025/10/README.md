# 2025 day 10

This serves purely as a means to jot down my thoughts and improvements of the original algorithm to get it into its
current state.

# attempt 0
Yes, I approached this with OOP. Just works better in my brain. Either way, my original approach was to do the
following:
- Keep the `target_light_indicator` as a list of `#` and `.`
- Keep each button as a light of integers
- For the `perform_toggles`, go with a priority queue, tracking
  - the number of presses done so far
  - the resulting light indicator

This approach was incredibly slow for the user input. So, I added an additional field to the PQ storing a global
counter value to speed up the PQ. This worked. Got the solution in around 33 secs.

However, this was still too slow for me.

# attempt 1
Taking this, I remembered a thought from earlier of representing the `target_light_indicator` and each `button` as
an integer, allowing for bitwise operators.

So, with this, I adapted the input parser to do that. With a base working, and refining the code, I settled on the
current:

```python
# Lights
target_light_indicator: int = 0
for indx, val in enumerate(given_target_light_indicator):
    if val == "#":
        target_light_indicator |= (1 << indx)

# Buttons
buttons: list[int] = []
for button in given_buttons:
    indexes: list[int] = list(map(int, button[1:-1].split(",")))

    button_mask: int = 0
    for indx in indexes:
        button_mask |= (1 << indx)

    buttons.append(button_mask)
```

Furthermore, I adapted the PQ to make use of XOR operations to determine the answer. This got the solution down to
~15s.

# attempt 2
The work now went to the PQ to optimise it. Ended up ditching it in favour of a BFS. This, paired with the bitwise
operations, brought the overall execution time down to ~0.01s. A much better improvement.
