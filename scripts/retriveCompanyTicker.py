import requests
import pandas as pd
import finnhub
import time
import yfinance as yf



def getTickerSymbol(company_name):
    api_key = "cj2qdbpr01qr0f6fqva0cj2qdbpr01qr0f6fqvag"
    base_url = "https://finnhub.io/api/v1/search"
    params = {
        "q": company_name,
        "token": api_key
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if "result" in data and data["result"]:
        # Finnhub may return multiple results, we will take the first one for simplicity
        ticker_symbol = data["result"][0]["symbol"]
        return ticker_symbol

    return None


def getTicker_AV(companyName):
    apiKey = "0BVMBOM0JVM1855A"
    base_url = "https://www.alphavantage.co/query"
    function = "SYMBOL_SEARCH"
    keywords = companyName
    params = {
        "function": function,
        "keywords": keywords,
        "apikey": apiKey
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    print(data)

    if "bestMatches" in data:
        best_matches = data["bestMatches"]
        if best_matches:
            return best_matches[0]["1. symbol"]

    return None


#for i in range(100):
#    print(getTickerSymbol('Phison Electronics'))
#    time.sleep(3)

if __name__ == '__main__':
    df = pd.read_csv('companies.csv')
    for i in range(len(df.index)):
        ticker = getTickerSymbol(df.loc[i, 'Company Name'])
        print(i, ticker, df.loc[i, 'Company Name'])
        df.loc[i, 'Symbol'] = ticker
    df.to_csv("companies_new.csv", index=False)



# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
"""
company = 'AAPL'
key = '0BVMBOM0JVM1855A'
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + company + '&apikey=' + key
r = requests.get(url)
data = r.json()
marketCap = data['MarketCapitalization']
print(marketCap)
"""
#wrQA1xJqzucjtQwZmfyc


# 0BVMBOM0JVM1855A