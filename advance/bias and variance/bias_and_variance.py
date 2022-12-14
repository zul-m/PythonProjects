# Train a machine learning model using the linear regression algorithm.
from mlxtend.evaluate import bias_variance_decomp
from sklearn.linear_model import LinearRegression
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error

import numpy as np
import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/zul-m/PythonProjects/main/student-mat.csv")
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"
x = np.array(data.drop([predict], axis = 1))
y = np.array(data[predict])

from sklearn.model_selection import train_test_split

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = 0.2)

linear_regression = LinearRegression()
linear_regression.fit(xtrain, ytrain)
y_pred = linear_regression.predict(xtest)

# Calculate bias and variance using Python.
mse, bias, variance = bias_variance_decomp(linear_regression, xtrain, ytrain, xtest, ytest, loss = 'mse', num_rounds = 200, random_seed = 123)

print("Average Bias:", bias)
print("Average Variance:", variance)