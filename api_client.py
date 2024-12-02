import requests

class DataImporterApiClient:
    BASE_URL = "https://api.restful-api.dev/objects"

    def fetch_objects(self):
        try:
            response= requests.get(self.BASE_URL)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occured: {e}")
            return None