## Get Stock Price Data

As machine learning practitioners, we need to collect stock price data for regression analysis and time series analysis. We can easily download it from [Yahoo Finance](https://finance.yahoo.com/?guccounter=1&guce_referrer=aHR0cHM6Ly90aGVjbGV2ZXJwcm9ncmFtbWVyLmNvbS8&guce_referrer_sig=AQAAAJbGp5yDcQJ1iryfVvpaewHzf55-TvBkc4z_fGwnpcx5ubsPTrEHwZFOGifgZ4E7N3sWcVE0l2Shj16eTO7cwPWRCJk-Yd9neP2s6nzRLVyxDeJ3o6cxfz3BQ0HGvoyNiKAaCFmQtQhxBT2ie8HZE62ugjMsIea2Qi4bX04rX33p). But imagine if we want to create an application where we can analyze the real-time stock prices, we need to collect the latest dataset instead of using the downloaded dataset. So if you want to learn how to get the stock price data between any time interval by using the Python programming language, this project is for you.

### Get Stock Price Data using Python

Yahoo Finance is one of the most popular websites to collect stock price data. You need to visit the website, enter the company’s name or stock symbol, and you can easily download the dataset. But if you want to get the latest dataset every time you are running your code, you need to use the `yfinance` API. `yfinance` is an API provided by Yahoo Finance to collect the latest stock price data.

To use this API, you need to install it by using the pip command in your terminal or command prompt as mentioned below.

```py
pip install yfinance
```

The code will collect the stock price data from today to the last 360 days. In this dataset, Date is not a column, it’s the index of this dataset. To use this data for any data science task, we need to convert this index into a column.

### Output

```
                  Open        High         Low       Close   Adj Close     Volume
Date
2021-12-09  174.910004  176.750000  173.919998  174.559998  173.552734  108923700
2021-12-10  175.210007  179.630005  174.690002  179.449997  178.414520  115402700
2021-12-13  181.119995  182.130005  175.529999  175.740005  174.725937  153237000
2021-12-14  175.250000  177.740005  172.210007  174.330002  173.324066  139380400
2021-12-15  175.110001  179.500000  172.309998  179.300003  178.265396  131063300

********************************

        Date        Open        High         Low       Close   Adj Close     Volume
0 2021-12-09  174.910004  176.750000  173.919998  174.559998  173.552734  108923700
1 2021-12-10  175.210007  179.630005  174.690002  179.449997  178.414520  115402700
2 2021-12-13  181.119995  182.130005  175.529999  175.740005  174.725937  153237000
3 2021-12-14  175.250000  177.740005  172.210007  174.330002  173.324066  139380400
4 2021-12-15  175.110001  179.500000  172.309998  179.300003  178.265396  131063300
```

### Summary

So this is how you can collect the latest stock price dataset between any time interval, using the Python programming language. If you want to get the latest dataset every time you are running your code, you need to use the `yfinance` API. `yfinance` is an API provided by Yahoo Finance to collect the latest stock price data.