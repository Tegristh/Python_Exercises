import time
import requests
from datetime import datetime
import config
import smtplib


MY_LAT = 45.799580
MY_LONG = 3.248590


def is_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    else:
        return False


def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False


def mail():
    if is_above() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=config.MY_MAIL, password=config.PASSWORD)
            connection.sendmail(
                from_addr=config.MY_MAIL,
                to_addrs=config.CIBLE,
                msg="Subject: ISS Above\n\n  ISS is above your position, look Up!!"
            )


while True:
    print(is_above(), is_night())
    mail()
    time.sleep(60)
