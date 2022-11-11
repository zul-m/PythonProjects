## Extract Keywords

Keywords play an important role when reading a long text to understand the subject and context of the text. Search engines also analyze an article’s keywords before indexing it. In this project, I will walk you through how to extract keywords using Python.

Well, we can also train a machine learning model that will extract keywords, but here I am just going to walk you through how to use a Python library for this task so that even beginners can understand how extracting keywords work before training a machine learning model.

### Extract Keywords using Python

There are so many Python libraries for the task of extracting keywords, the best ones are `spaCy`, `Rake-Nltk`, `YAKE`. In this project, I will use the `Rake-NLTK` as it is beginner-friendly and easy to install. You can easily install it by using the pip command;

```py
pip install rake-nltk
```

RAKE stands for Rapid Automatic Keyword Extraction. It is only built to extract keywords by using the NLTK library in Python. Now let’s see how to use this library for extracting keywords with first importing the Rake module from the rake-nltk library, store some text into a variable, and then extract the keywords from the text and print the output.

### Output

```
['rapid automatic keyword extraction algorithm', 'domain independent keyword extraction algorithm', 'determine key phrases', 'word appearance', 'rake short', 'words', 'tries', 'text', 'text', 'occurance', 'frequency', 'co', 'body', 'analyzing']
```

### Summary

The process of extracting keywords helps us identifying the importance of words in a text. This task can be also used for topic modelling. It is very useful to extract keywords for indexing the articles on the web so that people searching the keywords can get the best articles to read.

This technique is also used by various search engines. It is obvious that they don’t use any library but the process remains the same to extract keywords. You can learn how to train a machine learning model to extract keywords from [here](https://thecleverprogrammer.com/2020/12/01/keyword-extraction-with-python/).