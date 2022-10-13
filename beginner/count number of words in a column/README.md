## Count Number of Words in a Column

While working on a Data Science task, sometimes we have to deal with textual data. One of the problems beginners face while working on a textual dataset is counting the number of words in a piece of text. So if you want to learn how to count the number of words in a textual dataset, this project is for you.

### Count Number of Words in a Column using Python

Most data science professionals use the [pandas](https://thecleverprogrammer.com/2021/09/15/important-pandas-functions-for-data-science/) library for data handling and preparation. The pandas library doesn’t have any method to count the number of words in a piece of text. One way to solve this problem is by finding the length of the text by splitting the complete text.

So let’s import a [textual dataset](https://raw.githubusercontent.com/amankharwal/Website-data/master/articles.csv) where we can count the number of words in a column.

### Output

```
                                             Article                                              Title
0  Data analysis is the process of inspecting and...                  Best Books to Learn Data Analysis
1  The performance of a machine learning algorith...         Assumptions of Machine Learning Algorithms
2  You must have seen the news divided into categ...          News Classification with Machine Learning
3  When there are only two classes in a classific...  Multiclass Classification Algorithms in Machin...
4  The Multinomial Naive Bayes is one of the vari...        Multinomial Naive Bayes in Machine Learning
```

The dataset has two columns `Article` and `Title`. Let's create a new column as the number of words in the `Article` column.

```
                                             Article                                              Title  Number of Words
0  Data analysis is the process of inspecting and...                  Best Books to Learn Data Analysis               76
1  The performance of a machine learning algorith...         Assumptions of Machine Learning Algorithms               56
2  You must have seen the news divided into categ...          News Classification with Machine Learning               70
3  When there are only two classes in a classific...  Multiclass Classification Algorithms in Machin...               66
4  The Multinomial Naive Bayes is one of the vari...        Multinomial Naive Bayes in Machine Learning               96
```

So the dataset has three columns now, `Article`, `Title` and the `Number of Words` that contains the number of words in the article column.

### Summary

The pandas library doesn’t have any method to count the number of words in a piece of text. One way to solve this problem is by finding the length of the text by splitting the complete text. So, this is how you can count the number of words in any column while working on a textual dataset.