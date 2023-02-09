## Spelling Correction

Correcting spelling mistakes is an integral part of writing in the modern world, whether it is part of texting a phone, sending an email, writing large documents or searching for information on the web.

Modern spelling correctors aren’t perfect (indeed, automatic error correction is a popular source of fun on the web), but they’re ubiquitous in just about all software that relies on keyboard input.

Spelling correction is often viewed from two angles. Non-word spell check is the detection and correction of spelling mistakes that result in non-words. In contrast, real word spell checking involves detecting and correcting misspellings even if they accidentally result in a real English word (real word errors).

This can come from typographical errors of real-word errors (insertion, deletion, transposition) that accidentally produce a real word, or from cognitive errors where the writer substituted the wrong one.

### Spelling Correction with Python

The code in the directory is how to create a program for the task of Spelling correction with Python programming language.

### Output

```
Wrong words: ['Data Scence', 'Mahine Learnin']
Corrected Words are:
Data Science Machine Learning 
```

### Summary

With the use of [textblob](https://textblob.readthedocs.io/en/dev/) library in Python, we can easily create Machine Learning Models for the task of Spelling Corrections. Detecting actual word spelling errors is a much more difficult task, as any word in the input text can be an error. 

However, it is possible to use the noisy channel to find candidates for every word the user typed and rank the correction that was probably the user’s original intention.