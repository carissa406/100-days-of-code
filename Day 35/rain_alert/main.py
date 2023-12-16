
import requests 
from twilio.rest import Client

#print(f"api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}")

recovery_code = "G2QKLQ8XUVJFBLCRBY59J393"
OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"
api_key = "7eb92790447cd81ea88a9bbe9abc7085"
account_sid = "AC0ea8339a38c9b250f2e3bb823344b0bf"
auth_token = "3da4a37e7654ab253935fe1bb68f464d"
phone_number = ""

parameters = {
    "lat":47.177441,
    "lon":-122.292320,
    "appid": api_key,
    "cnt": 4
}


response = requests.get(OWM_Endpoint, params= parameters)
response.raise_for_status()
print(response)
data = response.json()

# day1 = data["list"][0]["weather"][0]["id"]
# print(day1)

will_rain = False

for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="Take an umbrella.",
                     from_='+18886228050',
                     to=phone_number
                 )
    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="No need for an umbrella.",
                     from_='+18886228050',
                     to=phone_number
                )
    print(message.status)


#use environment variables and hide api keys when there is sensitive information
