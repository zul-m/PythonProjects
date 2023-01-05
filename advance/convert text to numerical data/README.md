## Convert Text to Numerical Data

Text analysis is one of the major applications where machine learning algorithms are used. The process of converting textual data into numerical data is known as the process of vectorization in machine learning. It is an important task because you cannot use machine learning algorithms directly on a text as they only support numerical data.

Converting textual data to numeric data is not a difficult task as the [Scikit-learn](https://scikit-learn.org/stable/) library in Python provides so many methods for this task.

### Convert Text into Numerical Data using Python

I start this task by importing the `CountVectorizer` class from the `Scikit-learn` library in Python. Then, I store some texts into a Python list, and fit the list into the `CountVectorizer` function to convert the list of texts into numerical data.

Finally, as I have converted the textual data into numerical data, I present it in the form of a pandas DataFrame.

### Summary

The process of converting textual data into numerical data is known as vectorization in machine learning.