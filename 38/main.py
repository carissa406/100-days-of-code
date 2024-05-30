import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv

load_dotenv("C:/Users/hicks/Documents/Python/EnvironmentVariables/.env")
APP_ID = os.getenv("EXERCISE_APP_ID")
API_KEY = os.getenv("EXERCISE_API_KEY")
sheet_endpoint = os.getenv("EXERCISE_sheet_endpoint")

GENDER = os.getenv("GENDER")
WEIGHT_KG = int(os.getenv("WEIGHT_KG"))
HEIGHT_CM = int(os.getenv("HEIGHT_CM"))
AGE = int(os.getenv("AGE"))

USERNAME = os.getenv("EXERCISE_USERNAME")
PASSWORD = os.getenv("EXERCISE_PASSWORD")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
#-------------------------------------------------------------------------------------#

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        sheet_endpoint, 
        json=sheet_inputs, 
        auth=(
            USERNAME,
            PASSWORD
        ))

    print(sheet_response.text)