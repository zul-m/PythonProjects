## Validate Anagrams

An Anagram is a word or phrase that forms a different word or phrase when the letters of a word are rearranged. For example, the words `despair` and `praised` are anagrams.

### Validate Anagrams using Python

The validation of anagram words is one of the favourite questions in coding interviews. The idea is to write an algorithm to check if the input word creates a meaningful word when rearranged. So to validate an anagram using Python, we need to input two words and check if `word1` in any case matches `word2` after rearranging the words.

For example, the words `cinema` and `Iceman`, let’s say that the `word1` here is `cinema`, so we need to write an algorithm to check whether we can make the word `Iceman` after rearranging the letters of the word `cinema`.

In the code, I started with writing a Python function as `anagram` which includes two parameters `(word1, word2)`. Now while initializing the words, I converted them to lower case then I am checking if the `word1` equals the `word2` after sorting both the words.

### Output

```
True
True 
False
```

### Summary

So this is how we can validate the anagram words by using the Python programming language. It is one of the most important questions in any coding interviews.