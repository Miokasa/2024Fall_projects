import yfinance as yf

sp500 = yf.download('^GSPC', start="2014-11-01", end="2024-11-1")
sp500.to_csv('sp500_data.csv')

btc_data = yf.download("BTC-USD", start="2014-11-01", end="2024-11-1")
btc_data.to_csv("bitcoin_historical_data.csv")
