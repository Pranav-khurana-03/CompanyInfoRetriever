import requests
import pandas as pd
import finnhub
import time
import yfinance as yf
from urllib.error import HTTPError
import sys


class Company:
    def __init__(self, URL="", marketCap=0, sector="", revenue=0):
        self.URL = URL
        self.marketCap = marketCap
        self.sector = sector
        self.revenue = revenue


    def display(self):
        print(self.URL + str(self.marketCap) + str(self.sector) + str(self.revenue))

def getCompanyData(ticker):
    company = yf.Ticker(ticker)
    try:
        stockPrice = company.info['currentPrice']
        URL = company.info['website']
        outstandingShares = company.info['sharesOutstanding']
        marketCap = float(stockPrice) * int(outstandingShares)
        sector = company.info['industry']
        revenue = company.info['totalRevenue']
        return Company(URL, marketCap, sector, revenue)
    except:
        return Company()


if __name__ == '__main__':
    #getCompanyData('RTN2.BE').display()
    df = pd.read_csv('companies_new.csv')
    for i in range(len(df.index)):
        #print(df.loc[i, 'Symbol'])
        if not pd.isnull(df.loc[i, 'Symbol']):
            company = getCompanyData(str(df.loc[i, 'Symbol']))
            df.loc[i, 'Company Website'] = company.URL
            df.loc[i, 'Market Cap'] = company.marketCap
            df.loc[i, 'Market Segment'] = company.sector
            df.loc[i, 'Revenue'] = company.revenue
            df.loc[i, 'PublicPrivate'] = "Public"
        else:
            df.loc[i, 'PublicPrivate'] = "Private"
        
        #company.display()
    
    df.to_csv("companies_final.csv", index=False)
