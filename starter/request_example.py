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

get_request = requests.get('http://localhost:8000/')
response = requests.post('http://localhost:8000/', data=json.dumps(data))


print(get_request.status_code)
print(get_request.json())

print(response.status_code)
print(response.json())