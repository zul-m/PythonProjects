import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/zul-m/PythonProjects/main/beginner/box%20plot/advertising.csv")

print(data.head())

# Visualize a box plot using the Python programming language.
import plotly.express as px

fig = px.box(data, y = "TV")

fig.show()