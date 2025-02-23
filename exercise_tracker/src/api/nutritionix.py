import requests
from config.settings import HEADERS, GENDER, WEIGHT_KG, HEIGHT_CM, AGE

def get_exercise_data(query):
    parameters = {
        "query": query,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
    }

    response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", headers=HEADERS, json=parameters)
    response.raise_for_status()
    
    return response.json()
