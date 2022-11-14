## Create Acronyms

An acronym is a short form of a word created by long words or phrases such as NLP for natural language processing. In this project, I will walk you through how to write a program to create acronyms using Python.

### Create Acronyms using Python

To create acronyms using Python, you need to write a python program that generates a short form of a word from a given sentence. You can do this by splitting and indexing to get the first word and then combine it.

In the code, I am first taking a string user input, then I am using the `split()` function in Python for splitting the sentence. Then I declared a new variable `‘a’` to store the acronym of a phrase.

Then at the end, I am running a `for` loop over the variable `‘text’` which represents the split of user input. While running the `for` loop we are storing the index value of `str[0]`of every word after a split and turning it into an uppercase format by using the `upper()` function.

### Output

```
Enter a phrase: python projects
PP
```

### Summary

