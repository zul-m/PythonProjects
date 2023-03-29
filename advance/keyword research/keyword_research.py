import pandas as pd
import matplotlib.pyplot as plt

from pytrends.request import TrendReq

trends = TrendReq()

trends.build_payload(kw_list = ["Data Science"])
data = trends.interest_by_region()

print(data.sample(10))

df = data.sample(15)
df.reset_index().plot(x = "geoName", y = "Data Science", figsize = (120,16), kind = "bar")

plt.show()

data = trends.trending_searches(pn = "bulgaria")

print(data.head(10))

keyword = trends.suggestions(keyword = "Programming")
data = pd.DataFrame(keyword)

print(data.head())