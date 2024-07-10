import random
import requests
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "BAD4W17GXGI1B3KP"
NEWS_API_KEY = "7af39af7c3ad4a799940bf534af723f2"
YESTERDAY = None
OVERMORROW = None

EMAIL = "saymynameh4@gmail.com"
PASSWORD = "imrtaedndhzaskxl"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "extended_hours": False,
    "apikey": API_KEY
}

NEWS_PARAMETERS = {
    "q": "tesla",
    "from": OVERMORROW,
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY

}

stock_response = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMETERS)
stock_data = stock_response.json()
time_series = stock_data["Time Series (Daily)"]
count = 0
for date in time_series:
    if count == 0:
        YESTERDAY = time_series[date]["4. close"]
    elif count == 1:
        OVERMORROW = time_series[date]["4. close"]
        break
    count += 1


news_response = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMETERS)
news_data = news_response.json()
random_news = random.randint(0, 4)
title = news_data["articles"][random_news]["title"]
description = news_data["articles"][random_news]["description"]

print(f"Headline: {title}\nBrief: {description}")

percentage_change = ((float(YESTERDAY) - float(OVERMORROW)) / float(OVERMORROW)) * 100
if abs(percentage_change) <= 5:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs="shaikhzaidabdulrashid@gmail.com",
                            msg=f"Subject:{title}\n\n{description}"
                            )

