import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("https://raw.githubusercontent.com/zul-m/PythonProjects/main/beginner/visualize%20linear%20relationship/Instagram.csv", encoding = 'latin1')
data = data.dropna()

print(data.head())

# Here’s how to visualize linear relationships by using the plotly library in Python.
figure = px.scatter(data_frame = data,
                    x = "Impressions",
                    y= "Likes",
                    size = "Likes",
                    trendline = "ols",
                    title = "Relationship Between Likes and Impressions")

figure.show()

# To visualize linear relationships using matplotlib, you have to use seaborn.regplot method.
# So here’s how to plot linear relationships by using the matplotlib library in Python.
plt.figure(figsize = (10, 8))
plt.style.use('fivethirtyeight')
plt.title("Relationship Between Likes and Impressions")

sns.regplot(x = "Impressions", y = "Likes", data = data)

plt.show()