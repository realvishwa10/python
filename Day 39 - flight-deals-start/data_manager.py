import requests

SHEETY_URL = "https://api.sheety.co/4e2f6ec4542ffa3ae68fb1c09801659e/ghostFlightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def data_search(self):
        response = requests.get(url=SHEETY_URL)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_data(self):
        for city in self.destination_data:
            SHEETY_BODY = {
                "price": {
                    "iatacode": city["iataCode"]
                }
            }

            response = requests.post(url=f"{SHEETY_URL}/{city['id']}", json=SHEETY_BODY)
            response.raise_for_status()
