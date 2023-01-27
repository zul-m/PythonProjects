# Import the necessary Python dataset and libraries.
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_csv('google_play_store_reviews.csv')
df1.head()

# Create a word cloud with Python.
stopwords = set(STOPWORDS)
words = ''
for content in df1.Content:
    tokens = str(content).split()
    tokens = [i.lower() for i in tokens]
    
    words += ' '.join(tokens) + ' '
    
wordcloud = WordCloud(width = 800,
                height = 800,
                background_color = 'white',
                stopwords = stopwords,
                min_font_size = 10).generate(words)
  
# Plot the WordCloud image.
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()