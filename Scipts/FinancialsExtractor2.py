from yahoofinancials import YahooFinancials
import csv
import concurrent.futures
import yfinance as yf 
from datetime import date
from itertools import zip_longest
import numpy

'''While downloading data from the web, comment lines 108-156 and uncomment lines 13-104.
   While updating the close values in the same file, comment lines 13-91 and uncomment 103-147.
'''

symbol=0
remover=list()
tickers_list=list()

comp=csv.reader(open("Auto generated Dataset\Tickers.csv"))

for c in comp:
    tickers_list.extend(c)

def book_value_computer(ticker):

        try:
            #d=date.today()
            #d1=d.strftime('%Y-%m-%d')

            yahoo_financials=YahooFinancials(ticker)
            hold=yahoo_financials.get_key_statistics_data()
            hold2=yahoo_financials.get_summary_data()
            #close=yf.download(ticker,d1)['Adj Close']
            book_value=hold[ticker]['bookValue']
            EVtoEBITDA=hold[ticker]['enterpriseToEbitda']
            priceToBookR=hold[ticker]['priceToBook']
            market_cap=(hold2[ticker]['marketCap'])//10000000
            #print(book_value)    
            #print("\n")

        except:
            remover.append(ticker)
            print(remover)
        
        try:
            return ticker,book_value,EVtoEBITDA,priceToBookR,market_cap
        except:
            return ticker,None,None,None,None

with concurrent.futures.ThreadPoolExecutor() as executor:
 
    tickers=tickers_list[0:100]
    results=executor.map(book_value_computer,tickers)

    ticker_results=list()
    tickers_book_value=list()
    tickers_evtoebitda=list()
    tickers_priceToBook=list()
    tickers_marketcap=list()
    tickers_close=list()

    for result in results:
             
                ticker_results.append(result[0])
                tickers_book_value.append(result[1])
                tickers_evtoebitda.append(result[2])
                tickers_priceToBook.append(result[3])
                tickers_marketcap.append(result[4])
                #tickers_close.append(result[2])

                ''''print(ticker_results)
                print(tickers_book_value)
                print(tickers_evtoebitda)
                print(tickers_priceToBook)'''
                #print(tickers_close)
print("\n")
print("Final Outcome: ---------------------------------------------------------------------------------------------------")
print("\n")
'''print(ticker_results)
print(tickers_book_value)
print(tickers_evtoebitda)
print(tickers_priceToBook)
print(tickers_marketcap)'''
#print(tickers_close)

list_clubber=[ticker_results,tickers_book_value,tickers_evtoebitda,tickers_priceToBook,tickers_marketcap]
export_data=zip_longest(*list_clubber,fillvalue='')

with open("Auto generated Dataset\Financials.csv",'a',encoding="ISO-8859-1",newline='') as myfile:
    wr=csv.writer(myfile)
    #wr.writerow(("Ticker","Book Value"))
    wr.writerows(export_data)
myfile.close()

holder=list()

with open("Auto generated Dataset\Financials.csv",'r') as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        holder.append(row)
        if not row[1]:
            holder.remove(row)

with open("Auto generated Dataset\Financials.csv",'w',newline='') as fw:
    writer=csv.writer(fw)
    writer.writerows(holder)



'''ticker_names_reader=list()
ticker_book_values_reader=list()
ticker_evToEBITDA_reader=list()
ticker_priceToBook_reader=list()

with open("Auto generated Dataset\Financials.csv",'r') as csvfile:
 data = csv.DictReader(csvfile)
 print("---------------------------------")
 for row in data:
   ticker_names_reader.append(row['Ticker'])
   ticker_book_values_reader.append(row['Book Value'])
   ticker_evToEBITDA_reader.append(row['EvToEBITDA'])
   ticker_priceToBook_reader.append(row['PriceToBook'])

#print(ticker_names_reader)
#print(ticker_book_values_reader)

recent_closes=list() 

with open("Auto generated Dataset\Financials.csv",'r') as file1:
    csvreaderf=csv.reader(file1)
    for row in csvreaderf:
        if(row[0]=='Ticker'):
            continue 
        symbol=row[0]
        print(symbol)

        with open("Auto generated Dataset\{}.csv".format(symbol),'r') as file2:
            csv_inner_object=csv.reader(file2)
            hold=list()
            for line in csv_inner_object:
                hold.append(line[0:6])
            hold=hold[-1:]

            hold=numpy.column_stack(hold)
            close_type_nd=hold[4].astype(float)
            #print(type(close_type_nd))
            close_list=close_type_nd.tolist()
            recent_closes.extend(close_list)
    #print(recent_closes)

list_clubber_final=[ticker_names_reader,ticker_book_values_reader,ticker_evToEBITDA_reader,ticker_priceToBook_reader,recent_closes]
export_data_complete=zip_longest(*list_clubber_final,fillvalue='')

with open("Auto generated Dataset\Financials.csv",'w',encoding="ISO-8859-1",newline='') as myfile:
    wr=csv.writer(myfile)
    wr.writerow(("Ticker","Book Value","EV/EBITDA","P/BV","Close"))
    wr.writerows(export_data_complete)
myfile.close()'''





























'''holder=list()

with open('Financials.csv','r') as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        holder.append(row)
        if not row[1]:
            holder.remove(row)

with open('Financials.csv','w',newline='') as fw:
    writer=csv.writer(fw)
    writer.writerows(holder)'''


            

            



        
    
        



'''ticker="ADANITRANS.NS"
yahoo_financials=YahooFinancials(ticker)
hold=yahoo_financials.get_key_statistics_data()
print(hold)

print(hold['ADANITRANS.NS']['bookValue'])'''


