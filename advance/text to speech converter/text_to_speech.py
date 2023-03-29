# Import the libraries.
import nltk
import os

from newspaper import Article
from gtts import gTTS

# Get the article.
article = Article('https://hackernoon.com/future-of-python-language-bright-or-dull-uv41u3xwx')

article.download()
article.parse()

nltk.download('punkt')
article.nlp()

# Get the articles text.
mytext = article.text

language = 'en'

myobj = gTTS(text = mytext, lang = language, slow = False)

myobj.save("read_article.mp3")

os.system("start read_article.mp3")