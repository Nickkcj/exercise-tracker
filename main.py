import requests

APP_ID = "d0af2704"
APP_KEY = "efb096391fe49d8ae7e77965c4b404dc"
GENDER = "man"
WEIGHT_KG = 70
HEIGHT_CM = 180
AGE = 19

def get_info():
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": APP_KEY
    }
    exercise_text = input("Tell me which exercises you did: ")
    parameters = {
        "query": exercise_text,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE

    }
    
    response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", headers=headers, json=parameters)
    response.raise_for_status()
    print(response.json())

get_info()