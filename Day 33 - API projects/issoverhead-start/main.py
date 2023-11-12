import requests
from datetime import datetime
import smtplib

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
USER_NAME = "ghostyyyyyghost@gmail.com"
PASSWORD = "vgfuivloajnbbunh"

def iss_close():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    if MY_LAT-5 < iss_latitude < MY_LAT+5 and MY_LONG-5 < iss_longitude < MY_LONG+5:
        return True

# Your position is within +5 or -5 degrees of the ISS position.

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

    time_now = datetime.now()
    hour_now = time_now.hour

    if hour_now >= sunset or hour_now <= sunrise:
        return True

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


if iss_close():
    if is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=USER_NAME, password=PASSWORD)
            connection.sendmail(
                from_addr=USER_NAME,
                to_addrs="ghostyyyyyshot@yahoo.com",
                msg=f"Subject: LOOK UP!\n\nISS is above you!"
            )

