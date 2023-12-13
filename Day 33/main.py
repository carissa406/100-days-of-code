import requests
from datetime import datetime
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)

# response.raise_for_status() #raise exception if 404

# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]
# iss_position = (longitude, latitude)

# print(iss_position)

# #https://www.webfx.com/web-development/glossary/http-status-codes/

MY_LAT = 47.177441
MY_LNG = -122.292320

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise.split("T")[1].split(":")[0])

#time_now = datetime.now()
#print(time_now)