import datetime as dt
import random as rd
import smtplib

mail = "your-email@gmail.com"
password = "imrtaedndhzaskxl"

day = dt.datetime.now()
is_monday = day.weekday()

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=mail, password=password)
    if is_monday == 4:
        with open("crime_war_gangster_quotes.txt", "r") as file:
            quotes = file.readlines()
            quote = rd.choice(quotes)
            connection.sendmail(from_addr=mail,
                                to_addrs="sender-email@gmail.com",
                                msg=f"Subject: Stay Hard!\n\n{quote}"
                                )





