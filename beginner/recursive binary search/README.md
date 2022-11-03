## Recursive Binary Search

Recursion means solving problems by breaking down a complex problem into smaller problems and then solving it step by step. In this project, I will walk you through the implementation of the recursive binary search using Python, which means to implement the binary search algorithm using the recursive method.

[Binary search](https://thecleverprogrammer.com/2020/08/28/binary-search-algorithm-with-python/) means to find an item in a sorted array by repeatedly dividing the search interval into two halves and recursive binary search means to subdivide the entire binary search process into smaller problems. Simply put, the recursive solution to a binary search is known as a recursive binary search.

Here are the properties that all recursive solutions must satisfy:
 1. A recursive solution must have a base case.
 2. A recursive solution must have a recursive case.
 3. A recursive solution must make progress towards the base case.

A base case is a final case that represents the smallest subdivision of a complex problem. So according to the recursion properties above, to implement the recursive binary search, our algorithm must have a base case and a recursive case and the recursive case must progress to the base case otherwise the algorithm will never stop and will result in an infinite loop.

### Recursive Binary Search using Python

The binary search algorithm improves the search time required to locate an element in a sorted array. Usually, an iterative approach is followed to implement the binary search algorithm, but we can also implement it recursively by implementing it in smaller versions.

To implement the recursive binary search algorithm, we must first find the target in sorted order, the middle value is examined to determine if it is the target. If the middle value is not the target, the sequence is split in half, then the first or second half is examined to find the target value by looking at the middle element.

### Summary

Recursion is a very powerful tool for programming and problem-solving. It can be used to solve and implement a wide range of algorithms to solve basic iterative problems to advanced backtracking problems. In this project, we explored how to implement the recursive binary search algorithm using the Python programming language.