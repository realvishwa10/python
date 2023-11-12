# Birthday mail set up

import pandas
import random
import datetime as dt
import smtplib

now = dt.datetime.now()
current_month = now.month
current_day = now.day
today = (current_month, current_day)

my_email = "ghostyyyyyghost@gmail.com"
password = "vgfuivloajnbbunh"

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print(birthdays_dict)

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    random_letter = random.randint(1, 3)
    with open(f"letter_templates/letter_{random_letter}.txt") as file:
        content = file.read()
        new_content = content.replace("[NAME]", birthday_person["name"])
        print(new_content)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy birthday!!\n\n{new_content}"
        )


