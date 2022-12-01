import pandas as pd

movies = pd.read_csv("MoviesOnStreamingPlatforms_updated.csv")
movies['Rotten Tomatoes'] = movies["Rotten Tomatoes"].str.replace("%", "").astype(float)
movies.drop("Type", inplace = True, axis = 1)
correlations = movies.corr(method = 'pearson', numeric_only = True)

# Correlations between all features.
print(correlations)

# Correlations between a particular column "Year".
print(correlations["Year"])

# Visualizing correlations.
import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(correlations)
plt.show()