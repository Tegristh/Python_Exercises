import smtplib
import datetime as dt
import pandas as pd
import random
import os

# ⚠️⚠️⚠️ modify before git commit/pushing!!!⚠️⚠️⚠️
my_email = "mymail@gmail.com "
# target = "target_mail@gmail.com"
password = "secured_password"

peoples = pd.read_csv("people.csv", header=0).to_dict(orient="records")

birthday_today = []
now = dt.datetime.now()
today = now.day
this_month = now.month


def mail_to(name, target):
    file = random.choice(os.listdir("files"))
    with open(f"files/{file}", "r") as letter:
        new_letter = letter.read()
    message = f"Subject:Happy Birthday!\n\n" \
              f"{new_letter.replace('[NAME]', name)}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=target,
            msg=message
        )


for people in peoples:
    if people['month'] == this_month and people['day'] == today:
        mail_to(people['name'], people['email'])
