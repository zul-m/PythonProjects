import pandas as pd
import yfinance as yf
import datetime

from datetime import date, timedelta
today = date.today()

d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days = 360)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

data = yf.download('AAPL', start = start_date, end = end_date, progress = False)

print(data.head())

# Convert the date index into a column.
print("\n********************************\n")

data["Date"] = data.index
data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
data.reset_index(drop = True, inplace = True)

print(data.head())