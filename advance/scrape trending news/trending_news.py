# Scrape the latest trending news about Malaysia.
from GoogleNews import GoogleNews

news = GoogleNews(period = '1d')
news.search("Malaysia")
result = news.result()

# Convert the news into a pandas dataframe.
import pandas as pd

data = pd.DataFrame.from_dict(result)
# Drop the column "img" as it is of no use.
data = data.drop(columns = ["img"])
data.head()

# Run a `for` loop to get the complete link of the news arrticle.
for i in result:
    print("Title:", i["title"])
    print("News:", i["desc"])
    print("Read full news:", i["link"])