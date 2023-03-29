## Keyword Research

Google Trends is a keyword research tool that helps the researchers, bloggers, digital marketers and some more people in the digital industry to find how often a keyword is entered into Google search engine over a given period. Google Trends is used for keyword research mostly is writing articles on hot topics.

I use the Google API to access Google trends which can be done by using the `pytrends` library in python. Python being a general-purpose programming language provides libraries and packages for almost every task. `pytrends` can be easily installed by using the pip command;

```py
pip install pytrends
```

### Keyword Research with Python

You need to log in to Google first because, after all, we ask Google Trends for trending topics. For that, we need to import the method called `TrendReq` from the `pytrends.request` method.

### Keyword Interest By Region

I choose the term to search for as “Data Science”. Values ​​are calculated on a scale of 0 to 100, where 100 is the most popular location as a fraction of the total searches for that location, a value of 50 indicates a location half as popular. We can visualize the search results to get better insights.

### Summary

I hope you liked this project on Keyword research with python.