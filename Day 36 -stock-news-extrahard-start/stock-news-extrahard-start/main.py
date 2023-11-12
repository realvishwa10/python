import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
URL = "https://www.alphavantage.co/query"
PASS = "N4J7D3UKU3Y1C48Z"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": PASS
}

news_parameters = {
    "q": COMPANY_NAME,
    "apikey": "97e1c411f1a94eef8488763fe04689ca",
    "searchIn": "title"
}

stock_response = requests.get(url=URL, params=stock_parameters)
stock_response.raise_for_status()
data = stock_response.json()
dates_list = list(data["Time Series (Daily)"].keys())
recent_dates = dates_list[:2]
recent_stats = [data["Time Series (Daily)"][dates] for dates in recent_dates]
yesterday_price = float(recent_stats[0]["4. close"])
day_before_yesterday_price = float(recent_stats[1]["4. close"])
percent_increase = abs(((yesterday_price-day_before_yesterday_price)/yesterday_price)*100)
if 1 < percent_increase:
    print("Get news")
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    article_headline = [news_data["articles"][num]["title"] for num in range(0, 3)]
    article_data = [news_data["articles"][num]["description"] for num in range(0, 3)]
    for num in range(0, 3):
        print(f"Headline.{num+1}: {article_headline[num]}")
        print(f"Description. {num+1}: {article_data[num]}\n")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


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

