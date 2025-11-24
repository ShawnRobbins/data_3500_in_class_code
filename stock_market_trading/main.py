import requests
import json

tickers = ["AAPL", "TSLA", "NVDA", "SONY", "COST", "META", "AMZN", "SNAP", "DAL", "FIX"]

def inital_data_pull(ticker):
    # keys
    key1 = "Time Series (Daily)"
    key2 = "4. close"
    # date_key = "" # I know I need all the dates (maybe use an iterator variable???)

    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+ticker+"&outputsize=full&apikey=NG9C9EPVYBMQT0C8"

    request = requests.get(url)
    request_dictionary = json.loads(request.text)
    # print(request_dictionary)


    file = open("/workspaces/data_3500_in_class_code_FA_2025/stock_market_trading/"+ticker+".csv", "w")

    lines = []

    for date in request_dictionary[key1].keys():
        lines.append(date + ", " + request_dictionary[key1][date][key2] + "\n")

    lines = lines[::-1]
    file.writelines(lines)
    file.close()


# for ticker in tickers:
#     inital_data_pull(ticker)

def append_data(ticker):
    # keys
    key1 = "Time Series (Daily):"
    key2 = "4. close"

    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+ticker+"&apikey=NG9C9EPVYBMQT0C8"

    request = requests.get(url)
    request_dictionary = json.loads(request.text)

    # print(request_dicitonary)

    with open("stock_market_trading/AAPL.csv") as file:
        lines = file.readlines()

    recentest_date = lines[-1].split(", ")[0]
    
    new_lines = []
    for date in request_dictionary[key1].keys():
        if date > recentest_date:
            new_lines.append(date + ", " + request_dictionary[key1][date][key2] + "\n")

    new_lines = new_lines[::-1]

    with open("/workspaces/data_3500_in_class_code/stock_market_trading/"+ticker+".csv", "a") as file:
        file.writelines(new_lines)

for ticker in tickers:
    append_data(ticker)

