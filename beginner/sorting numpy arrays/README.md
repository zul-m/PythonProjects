## Sorting NumPy Arrays

Being a computer science student you must have gone through the concept of sorting algorithms. In Python, we use sorting algorithms to sort items in a list. But what if we want to sort NumPy arrays?

There are a bunch of sorting algorithms in computer science, for example:
 1. Insertion Sort
 2. Selection Sort
 3. Merge Sort
 4. Bubble Sort and many more.

All of these algorithms are used to sort values in a list or an array. The NumPy library provides an inbuild function for sorting the values inside a NumPy array. Below is how we sort a NumPy array by using the inbuilt sort function:

```py
import numpy as np
a = np.array([34, 5, 89, 23, 76])
print(np.sort(a))
```

The sort function in the NumPy library works the same as the sort function in the Python programming language. But, what if we want to write a sorting algorithm to sort a NumPy array using Python without using the sort function?

### Sort NumPy Arrays using Python

Sorting values in a data structure is one of the favourite topics of coding interviews. NumPy array is also a data structure like a list or an array, so you should also know how to sort the values of a NumPy array using Python without using any sort function.
### Output

```
[ 5 23 34 76 89]
```

### Summary

The above algorithm is based on the selection sort. It is a very common algorithm for sorting values in a data structure.