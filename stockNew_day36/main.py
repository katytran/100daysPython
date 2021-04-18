import datetime
import requests
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "S5L4EBSTI0IU9K2L"
NEW_API_KEY = "eea74ab76b1a4d13b0822b68e8f136de"

parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY

}

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
daybefore = today - datetime.timedelta(days=2)


#Get close stock data
response = requests.get(STOCK_ENDPOINT, params=parameter)
response.raise_for_status()
stock_close_yesterday = response.json()["Time Series (Daily)"][f"{yesterday}"]["4. close"]
stock_close_daybefore = response.json()["Time Series (Daily)"][f"{daybefore}"]["4. close"]
percent_difference = (float(stock_close_yesterday)-float(stock_close_daybefore))/float(stock_close_yesterday) *100
print(stock_close_yesterday)
print(stock_close_daybefore)
print(round(percent_difference, 2))

#if difference is 0.1%
#get new
if(abs(percent_difference) >= 0.1):
    url = ('https://newsapi.org/v2/everything?'
           f"q={STOCK}&"
           f"from={today}&"
           'sortBy=popularity&'
           f"apiKey={NEW_API_KEY}")

    response_new = requests.get(url)
    response_new.raise_for_status()
    list_article = response_new.json()['articles'][:3]

    for article in list_article:
        headline = article["title"]
        content = article["content"][0:150]+"..."
        url = article["url"]
        print(headline, content, url)







## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

