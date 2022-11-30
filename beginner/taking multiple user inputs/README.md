## Taking Multiple User Inputs

The `input()` function of Python help us to give a user input while writing a program. But how to take multiple user inputs in the terminal? In this project, I will take you through how to take multiple user inputs with Python by using a `while` loop.

### Problem Statement for Taking Multiple User Inputs with Python

Suppose you are prompted to write a Python program that interacts with a user in a console window. You may be accepting input to send to a database, or reading numbers to use in a calculation.

Whatever the purpose, you should code a loop that reads one or multiple user inputs from a user typing on a keyboard and prints a result for each. In other words, you have to write a classic print loop program.

### Multiple Inputs with Python using While Loop

Now let’s see how to solve the above problem statement by taking multiple inputs with Python using a while loop.

The code leverages the Python `while` loop, Python’s most general loop statement. The built-in `input` function is used here for general console input, it prints its optional argument string as a prompt, and returns the response entered by the user as a string.

A single-line `if` statement that uses the special rule for nested blocks also appears here. The body of the `if` statement appears on the header row after the colon instead of being indented on a new row below.

Finally, the Python `break` statement is used to exit from the `while` loop statement immediately. It simply jumps out of the `while` loop statement and the program continues after the loop. Without this exit statement, the `while` would loop forever, because its test is still `True`.

### Output

```
Enter text: hello
Enter text: my name is Zulfikar
Enter text: how are you
Enter text: stop
stop
```

### Summary

I hope you liked this project on how to take multiple user inputs with [Python](https://www.python.org/) by using a while loop.