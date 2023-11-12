import smtplib
import random
import datetime as dt

with open("quotes.txt") as file:
    data = file.readlines()

quote = random.choice(data)

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 6:
    my_email = "ghostyyyyyghost@gmail.com"
    password = "vgfuivloajnbbunh"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ghostyyyyyghost@yahoo.com",
            msg=f"Subject: Quote for the day\n\n{quote}"
        )
