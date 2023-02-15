## Monty Hall Problem

The Monty Hall Problem is a well-known puzzle derived from an American game show, “Let’s Make a Deal”. The intuition behind this game leads many people to get it wrong, and when the Monty Hall issue is featured in a newspaper or discussion list, it often leads to a long argument in letters to the editor and on bulletin boards

The Monty Hall Problem is like this:
 1. The show has three doors. A prize like a car or vacation is behind a door, and the other two doors hide a worthless prize called a Zonk; in most discussions of the problem, the Zonk is a goat.
 2. The competitor chooses a door. We’ll assume that the entrant has no internal knowledge of which gate is holding the prize, so the entrant will simply make a random choice.
 3. Smiling host Monty Hall opens one of the other doors, always choosing the one that shows a goat, and always offers the contestant a chance to change their choice for the remaining unopened door.
 4. The competitor chooses to change the gate or chooses to stick to the first choice.

### Simulating Monty Hall Problem with Python

Simulating the Monty Hall problem with Python is simple. We will write a function that uses Python’s `random` module to choose which door hides the price, the competitor’s initial choice, and which doors Monty chooses to open.

An input parameter controls whether the competitor chooses to change, and the function will then return a boolean indicating whether the competitor’s final choice was the winning gate.

### Output

```
Winning percentage without changing choice: 0.333382
Winning percentage while changing choice: 0.666618
```

### Summary

I hope you liked this project on simulating the Monty Hall problem with Python programming language.