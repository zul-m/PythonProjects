# Import all libraries and a dataset with textual information.
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from wordcloud import STOPWORDS

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("spam.csv")

print(data.head())

# Visualize a word cloud from the text column of the dataset.
text = " ".join(i for i in data.text)
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords = stopwords, background_color = "white").generate(text)

plt.figure(figsize = (15, 10))
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")

plt.show()