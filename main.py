import pandas
import requests
import datetime
import csv
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
params_stock = {
 "function" :"TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": "CUOMF33Z1P0OMUZL",
}
params = {
    "q": "TSLA",
    "apiKey": "bacfb1a30d5346f2a17d0d0a00f20918",

}

previous_Date = datetime.date.today() - datetime.timedelta(days=2)
current_date_in_us = datetime.date.today() - datetime.timedelta(days=1)
previous_Date_str = datetime.date.isoformat(previous_Date)
current_date_in_us_str =datetime.date.isoformat(current_date_in_us)
print(previous_Date_str)
print(current_date_in_us_str)
if previous_Date.isoweekday() == 6:
    previous_Date = datetime.date.today() - datetime.timedelta(days=3)
elif previous_Date.isoweekday() == 7:
    previous_Date = datetime.date.today() - datetime.timedelta(days=3)
elif current_date_in_us.isoweekday() == 6:
    current_date_in_us = datetime.date.today() - datetime.timedelta(days=2)
elif current_date_in_us.isoweekday() == 7:
    current_date_in_us = datetime.date.today() - datetime.timedelta(days=3)





else:
    stock_reponse = requests.get("https://www.alphavantage.co/query", params_stock)
    print(stock_reponse.raise_for_status())
    stock_data = stock_reponse.json()
    print(stock_data)
    previous_Date_data = (stock_data["Time Series (Daily)"][previous_Date_str]["4. close"])
    current_date_data = (stock_data["Time Series (Daily)"][current_date_in_us_str]["4. close"])
    price_change = (float(current_date_data) - float(previous_Date_data))
    percentage_change = (float(price_change) / float(current_date_data)) * 100
    change = ( "%.2f" % percentage_change)
    print(f"the price has been change {change} %")

    if float(change) > 0 and float(change) > float(1):
        print(f"something happen big in tesla stock the price is {change} % Up from yestarday close ")
        with open("title.csv") as filedata:
            datax = pandas.DataFrame(filedata)
            # list of news to send to the client
            formated_list = [datax[0][i]for i in datax.index]


    elif float(change) < 0 and float(change) > float(-1):
        print(f"something happen big in tesla stock the price is {change} % Up from yestarday close ")
        with open("title.csv") as filedata:
            datax = pandas.DataFrame(filedata)
            formated_list = [datax[0][i] for i in datax.index]



response = requests.get("https://newsapi.org/v2/everything",params= params)
print(response.raise_for_status())
data = (response.json())
article =(data["articles"][:5])
titles =[ article[i]["title"] for i in range(len(article))]
headlines = titles[:3]
with open("title.csv", "w") as file:
     write = csv.writer(file, lineterminator = '\n')
     write.writerows([i.split(",")for i in headlines])
     file.close()

 
