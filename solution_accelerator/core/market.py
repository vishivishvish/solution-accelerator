import yfinance as yf


def get_market_history(ticker):
    data = yf.Ticker(ticker)
    hist = data.history(period="7d")
    return hist["Close"]
