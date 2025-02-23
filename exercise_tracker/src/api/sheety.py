import requests
import datetime
from config.settings import HEADERS, SHEET_ENDPOINT

def add_exercise_to_sheet(exercise_data):
    for exercise in exercise_data["exercises"]:
        parameters = {
            "workout": {
                "date": datetime.datetime.now().strftime("%d/%m/%Y"),
                "time": datetime.datetime.now().strftime("%H:%M:%S"),
                "exercise": exercise["name"],
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }

        response = requests.post(url=SHEET_ENDPOINT, json=parameters, headers=HEADERS)
        response.raise_for_status()
        
