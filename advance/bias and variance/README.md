## Bias and Variance

When training a machine learning model, it is very important to understand the [bias and variance](https://thecleverprogrammer.com/2020/12/28/bias-and-variance-in-machine-learning/) of predictions of your model. It helps in analyzing prediction errors which help us in training more accurate machine learning models.

### What are Bias and Variance?

Bias is the difference between predicted values and expected results. A machine learning model with a low bias is a perfect model and a model with a high bias is expected with a high error rate on the training and test sets.

Variance is the variability of your model’s predictions over different sets of data. A machine learning model with high variance indicates that the model may work well on the data it was trained on, but it will not generalize well on the dataset it has never seen before.

### Bias and Variance using Python

You must be using the `scikit-learn` library in Python for implementing most of the machine learning algorithms. But it does not have any function to calculate the bias and variance of your trained model. So to calculate the bias and variance of your model using Python, you have to install another library known as `mlxtend`. You can easily install it in your system by using the pip command.

```py
pip install mlxtend
```

### Output

```

```

### Summary

Bias is the difference between predicted values and expected results. Variance is the variability of your model’s predictions over different sets of data.