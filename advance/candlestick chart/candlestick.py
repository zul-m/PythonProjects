import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv("AAPL.csv")

figure = go.Figure(data = [go.Candlestick(
    x = data["Date"], open = data["Open"], high = data["High"],
    low = data["Low"], close = data["Close"])]
)
figure.update_layout(title = "Apple Stock Price Analysis", xaxis_rangeslider_visible = False)

figure.show()