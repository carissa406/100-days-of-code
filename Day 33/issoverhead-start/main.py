import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 47.177441
MY_LONG = -122.292320
MY_EMAIL = "catentertainers@gmail.com"
MY_PASSWORD = "stsu muqc tbbf mwwu"

def close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.

    if MY_LAT-5<=iss_latitude <=MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

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

    #If the ISS is close to my current position
    
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)

    if close() and is_night():


        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:

                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, 
                                    to_addrs="hicks.carissa@gmail.com", 
                                    msg=f"Subject:Sunset\n\nLook Up")




