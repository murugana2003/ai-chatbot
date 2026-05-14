import yfinance as yf

ticker = yf.Ticker("AAPL")

data = ticker.history(period="5d")

print(data)
print("Latest close:", data["Close"].iloc[-1])