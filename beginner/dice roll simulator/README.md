## Dice Roll Simulator

The Dice Roll Simulation can be done by choosing a random integer between 1 and 6 for which we can use the [random](https://docs.python.org/3/library/random.html) module in the Python programming language. In this project, I will take you through how to create a Dice Roll Simulator with Python.

### Dice Roll Simulator with Python

To simulate a dice roll with Python, I’ll be using the `random` module in Python. The `random` module can be imported easily into your code as it is preinstalled in the Python programming language.

After importing the `random` module, you have access to all the functions included in the module. It’s a pretty long list, but for our purposes, we’ll use the `random.randint()` function. This function returns a random integer based on the start and end we specify.

The smallest value of a dice roll is `1` and the largest is `6`, this logic can be used to simulate a dice roll. This gives us the start and end values to use in our `random.randint()` function.

### Output

```
Rolling the dices...
The values are: 
6
5
Roll the dices again (y/N): y
Rolling the dices...        
The values are: 
5
4
Roll the dices again (y/N): y
Rolling the dices...        
The values are: 
1
2
Roll the dices again (y/N): 
```

## Summary

This is a good task for someone beginner in Python to start with. These type of programs helps you to think logically and in the long run, it can also help you to create algorithms.