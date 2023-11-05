import requests
from twilio.rest import Client

MY_LAT = 13.082680
MY_LONG = 80.270721
ID_PASS = "ce88af2759c1105582176b38f628dad3"
ACCOUNT_SID = "ACaefa7088299b547598f59f4bafd54adc"
AUTH_TOKEN = "63d9634acc7cce8bddc29019a8d66588"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": ID_PASS,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.8/onecall", params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) > 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body="It is very sunny today",
        from_='+13342342102',
        to='+916381449329'
    )
    print(message.status)
