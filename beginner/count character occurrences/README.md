## Count Character Occurrences

Counting occurrences of a character in a string means counting all substrings of a character from the input string. This is one of the important questions you are asked in the coding interviews.

### Count Character Occurrences using Python

To count the occurrences of a character, we need to write an algorithm that returns the number of times each character appears in the input string. The algorithm must iterate through each character from the beginning to count the number of times each character appears in the string.

In the code, we step through each character in the input string. If the character is already present in the string, we simply increment the value of the character by 1 and so on. Otherwise, we just add the character in the dictionary and set it to 1. In the end, we get a dictionary with the characters as keys and their values as the number of times they appeared in the string.

### Output

```
{'P': 2, 'y': 1, 't': 2, 'h': 1, 'o': 2, 'n': 1, 'r': 1, 'j': 1, 'e': 1, 'c': 1, 's': 1}
```

### Summary

Counting the occurrences of a character is an important question for the coding interview. Here we have to write an algorithm to count the number of times each character appears in a string.