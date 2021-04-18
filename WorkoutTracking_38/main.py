import requests
import json
import datetime
import _strptime

APP_ID = "1e9eafdc"
API_KEY = "cec7284fb75b84c53dc1462a2c6fe720"
BASE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
BASE_URL_SHEET = "https://api.sheety.co/ef3139395c1209202a3fc6e628eb4a9a/oppaWorkouts/workouts"

GENDER = "male"
WEIGHT_KG = 72
HEIGHT_CM = 179
AGE = 27

exercise = input("What exercises you did today?")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameter = {
 "query": exercise,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age": AGE,
}

response = requests.post(BASE_URL, parameter, headers=headers)
response.raise_for_status()
print(json.dumps(response.json(), indent=4, sort_keys=True))

exercise_list = response.json()['exercises']
for exercise in exercise_list:
    exercise_name = exercise['name']
    duration = exercise['duration_min']
    calories = exercise['nf_calories']
    today = datetime.datetime.now()
    today_format = today.strftime("%d/%m/%Y")
    time_format = today.strftime("%X")

    body = {
        "workout": {
            "date": today_format,
            "time": time_format,
            "exercise": exercise_name.title(),
            "duration": duration,
            "calories": calories,
        }
    }

    response_sheety = requests.post(BASE_URL_SHEET, json=body)
    print(response_sheety.text)

    response_sheety = requests.get("https://api.sheety.co/ef3139395c1209202a3fc6e628eb4a9a/oppaWorkouts/workouts", json=body)
    print(response_sheety.text)









