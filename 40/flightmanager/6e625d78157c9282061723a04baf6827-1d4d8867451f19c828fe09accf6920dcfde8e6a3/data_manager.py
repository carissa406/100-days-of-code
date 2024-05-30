import requests
import os

SHEET_ENDPOINT = os.getenv("FLIGHT_SHEET_ENDPOINT")
USERNAME = os.getenv("EXERCISE_USERNAME")
PASSWORD = os.getenv("EXERCISE_PASSWORD")

def get_customer_emails(self):
    customers_endpoint = SHEET_ENDPOINT
    response = requests.get(customers_endpoint)
    data = response.json()
    self.customer_data = data["users"]
    return self.customer_data