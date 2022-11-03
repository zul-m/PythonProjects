## Swap Variables

Swapping variables means assigning the value of `variable` a to `variable b` and vice versa. We have so many algorithms in computer science for swapping the values of two variables with each other, so in this project, I’m going to walk you through how to swap variables using Python.

### Swap Variables using Python

We have so many algorithms in computer science to swap variables but the easiest ones are:
 1. Swapping two variables by introducing another variable
 2. Swapping variables by simply assigning them to each other

Let’s see how to swap two variables using Python by introducing a new variable on `swapping_1.py`. In the code, I have first declared two variables as `a = 8`, and `b = 10`. Then I am introducing another variable as `c = a` which means that I am assigning the value of `a` to `c` then in the next line I assign the value of `b` to `a`. Till now we have `c = a`, and `a = b`, and `b = 10`. So in the next line, I am assigning the value of `c` to `b`. In the end, we are left with `a = 10`, `b = 8`.

Now let’s see how to use the other method of swapping variables which is to swap the values of variables with each other without introducing another variable on `swapping_2.py`. We cannot assign the values of variables to each other line by line as we did in the above method, because if we write `a = b` in the first line and `b = a`, in the second line then we will end up having `a = 10`, and `b = 10, as in the first line we are assigning b to a which means we are assigning `10` to `a`, then in the next line, we are assigning `a` to `b` i,e. `10` to `b` again. So to swap two variables without introducing a new variable we have to swap them in one line only as shown in the code.

### Output

```
a = 10
b = 8
```

### Summary

So this is how we can swap the values of 1 variable with another variable. You can use the same method to swap lists, dictionaries, sets and tuples also instead of just numerical values.