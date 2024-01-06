import requests
import os
from dotenv import load_dotenv
load_dotenv("C:/Users/hicks/Documents/Python/EnvironmentVariables/.env")

SHEET_ENDPOINT = os.getenv("FLIGHT_SHEET_ENDPOINT")
USERNAME = os.getenv("EXERCISE_USERNAME")
PASSWORD = os.getenv("EXERCISE_PASSWORD")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        
    def get_destination_data(self):
        response = requests.get(
        url = SHEET_ENDPOINT,
        auth=(
            USERNAME,
            PASSWORD
        ))
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEET_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)