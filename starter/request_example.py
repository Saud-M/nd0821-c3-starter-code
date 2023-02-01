import json
import requests

data = {
    "age": 24,
    "workclass": "State-gov",
    "fnlgt": 483777,
    "education": "Bachelors",
    "education_num": 13,
    "marital_status": "Married-civ-spouse",
    "occupation": "Exec-managerial",
    "relationship": "Husband",
    "race": "White",
    "sex": "Female",
    "capital_gain": 0,
    "capital_loss": 0,
    "hours_per_week": 40,
    "native_country": "United-States"
}

endpoint = "https://employees-model-udacity.onrender.com/"
get_request = requests.get(endpoint)
response = requests.post(endpoint, data=json.dumps(data))


print(f"Endpoint: {endpoint}")
print(f"GET: {get_request.status_code}")
print(get_request.json())
print(f"POST: {response.status_code}")
print(response.json())