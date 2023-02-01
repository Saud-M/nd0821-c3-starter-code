import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_root():
    request = client.get('/')
    assert request.status_code == 200
    assert request.json() == {"message": "Main GET page"}

def test_post_less_and_equal_50k():
# 38,Private,215646,HS-grad,9,Divorced,Handlers-cleaners,Not-in-family,White,Male,0,0,40,United-States,<=50K

    data = {
        "age": 38,
        "workclass": "Private",
        "fnlgt": 215646,
        "education": "HS-grad",
        "education_num": 9,
        "marital_status": "Divorced",
        "occupation": "Handlers-cleaners",
        "relationship": "Not-in-family",
        "race": "White",
        "sex": "Male",
        "capital_gain": 2174,
        "capital_loss": 0,
        "hours_per_week": 40,
        "native_country": "United-States"
    }
    r = client.post("/", data=json.dumps(data))
    assert r.status_code == 200
    assert r.json() == "<=50K"

def test_post_sample_greater_than_50K():
# 42,Private,159449,Bachelors,13,Married-civ-spouse,Exec-managerial,Husband,White,Male,5178,0,40,United-States,>50K

    data = {
        "age": 42,
        "workclass": "Private",
        "fnlgt": 159449,
        "education": "Bachelors",
        "education_num": 13,
        "marital_status": "Married-civ-spouse",
        "occupation": "Exec-managerial",
        "relationship": "Husband",
        "race": "White",
        "sex": "Male",
        "capital_gain": 5178,
        "capital_loss": 0,
        "hours_per_week": 45,
        "native_country": "United-States"
    }
    r = client.post("/", data=json.dumps(data))
    assert r.status_code == 200
    assert r.json() == ">50K"