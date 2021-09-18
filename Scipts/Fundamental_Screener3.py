import csv
import traceback
import numpy
from itertools import zip_longest
from yahoofinancials import YahooFinancials
import smtplib
import math
from more_itertools import unique_everseen

tickers_name=list()
tickers_PTS=list()
tickers_MCap=list()
tickers_bookval=list()
tickers_close=list()

with open("Auto generated Dataset\FinancialsBunch.csv",'r') as mf:
    data=csv.DictReader(mf)

    for row in data:

        try:
            hold2=float(row['PToSales'])
            hold2=round(hold2,3)
            #print(hold2<1)

        except Exception as e:
            print(row['Ticker'])
            print(traceback.format_exc())

        if(hold2<1):
                tickers_name.append(row['Ticker'])
                tickers_MCap.append(row['MarketCap'])
                tickers_PTS.append(row['PToSales'])
                tickers_close.append(row['Close'])
                tickers_bookval.append(row['Book Value'])


list_clubber=[tickers_name,tickers_MCap,tickers_PTS,tickers_close,tickers_bookval]
export_data_complete=zip_longest(*list_clubber,fillvalue='')

with open("Auto generated Dataset\MCapPTS.csv",'w',encoding="ISO-8859-1",newline="") as myfile:
    wr=csv.writer(myfile)
    wr.writerow(("Ticker","Market Cap","P/S","LTP","Book Value"))
    wr.writerows(export_data_complete)
    print("Execution Success!")