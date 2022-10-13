import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/zul-m/PythonProjects/main/beginner/count%20number%20of%20words%20in%20a%20column/articles.csv", encoding = 'latin1')

print(data.head())

# Let's create a new column as the number of words in the article column.
data["Number of Words"] = data["Article"].apply(lambda n: len(n.split()))

print(data.head())