import yfinance as yf 
import csv

comp=csv.reader(open("Auto generated Dataset\Tickers.csv"))

for c in comp:

    symbol=c[0]

    history_filename="Auto generated Dataset\{}.csv".format(symbol)

    f=open(history_filename,'w',newline="")

    ticker=yf.Ticker(symbol)
    df=ticker.history(period='1mo')

    f.write(df.to_csv())
    f.close()
print("Execution successful")