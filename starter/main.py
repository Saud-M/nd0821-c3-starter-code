# Put the code for your API here.
import os
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field
import pickle
from starter.ml.model import inference
from starter.ml.data import process_data

app = FastAPI()
file_dir = os.path.dirname(__file__)
model_path = os.path.join(file_dir, 'model/rf_model.pkl')
encoder_path = os.path.join(file_dir, 'model/encoder.pkl')
lb_path = os.path.join(file_dir, 'model/lb.pkl')



class Data_sample(BaseModel):
	# Using the first row of census.csv as sample
	# 39,State-gov,77516,Bachelors,13,Never-married,Adm-clerical,Not-in-family,White,Male,2174,0,40,United-States
    age: int = Field(None, example=39)
    workclass: str = Field(None, example='State-gov')
    fnlgt: int = Field(None, example=77516)
    education: str = Field(None, example='Bachelors')
    education_num: int = Field(None, example=13)
    marital_status: str = Field(None, example='Never-married')
    occupation: str = Field(None, example='Adm-clerical')
    relationship: str = Field(None, example='Not-in-family')
    race: str = Field(None, example='White')
    sex: str = Field(None, example='Male')
    capital_gain: int = Field(None, example=2174)
    capital_loss: int = Field(None, example=0)
    hours_per_week: int = Field(None, example=40)
    native_country: str = Field(None, example='United-States')


@app.get('/')
async def main_page():
	return "Main GET page"

@app.post('/')
async def predict(sample: Data_sample):
	sample = {key.replace('_', '-'): [value] for key, value in sample.__dict__.items()}
	data = pd.DataFrame.from_dict(sample)

	cat_features = [
		"workclass",
		"education",
		"marital-status",
		"occupation",
		"relationship",
		"race",
		"sex",
		"native-country",
	]

	X, _, _, _ = process_data(data, categorical_features=cat_features, label=None, 
	training=False, encoder=encoder, lb=lb)

	pred = inference(model, X)[0]
	return '<=50K' if pred == 0 else '>50K'