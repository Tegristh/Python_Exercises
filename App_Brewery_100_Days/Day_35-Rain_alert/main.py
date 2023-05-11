import requests
import env
from twilio.rest import Client


# ------------------------------- Twilio Api ---------------------------------------#

account_sid = "[My_sid]"
auth_token = env.AUTH_TOKEN
client = Client(account_sid, auth_token)


# ------------------------------ OpenWeatherMap Api ------------------------------------- #

# https://api.openweathermap.org/data/3.0/onecall?lat=45.799580&lon=3.248590&appid=b0ce4ea353539e49d37f294d56f3c1bc
URL = "https://api.openweathermap.org/data/3.0/onecall"
MY_LAT = 45.799580
MY_LONG = 3.248590
MY_API_KEY = env.MY_API_KEY
MY_TWILIO_NUMBER = "[My_Twilio_Number]"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": 'current,minutely,daily,alerts',
    "appid": MY_API_KEY,
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()

data = response.json()['hourly']
will_rain = False
weather_slice = data[:12]
for hour_data in weather_slice:
    condition_code = int(hour_data["weather"][0]['id'])

    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an Umbrella",
            from_=MY_TWILIO_NUMBER,
            to=env.MY_NUMBER,
        )
    print(message.status)
