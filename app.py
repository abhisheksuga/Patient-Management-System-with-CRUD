from fastapi import FastAPI
import pickle
import pandas as pd
from fastapi.responses import JSONResponse 
from schema.user_input import UserInput
from schema.results_reponse import ResultResponse
from model.predict import predict_output , MODEL_VERSION


app =FastAPI()



@app.get('/')
def home():
    return{'message':'Welcome to the Insurance Premium Prediction System'}

#endpoint for the services like ELB / Kub
@app.get('/health')
def health_check():
    return{'status':'Ok' ,'version':MODEL_VERSION}


@app.post('/predict',response_model=ResultResponse)
def predict_premium(data : UserInput):


    input_df = {
        'bmi' : data.bmi,
        'age_group' : data.age_group ,
        'lifestyle_risk' : data.lifestyle_risk ,
        'city_tier' : data.city_tier,
        'income_lpa' :data.income_lpa ,
        'occupation' : data.occupation

    }
    try:

        prediction = predict_output(input_df)
        
        return JSONResponse(status_code=200,content={'predicted_category':prediction})
    except Exception as e :
        return JSONResponse(status_code=500 ,content=str(e))
