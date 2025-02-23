import os

BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
GENDER = "man"
WEIGHT_KG = 70
HEIGHT_CM = 180
AGE = 19

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "Content-Type": "application/json"
}
