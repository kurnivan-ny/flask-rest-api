import pprint
import requests

data = {
    "age":20, "avg_glucose_level":100, "bmi":30, "gender":"male", "hypertension":"no", "heart_disease":"yes", "ever_married":"no","work_type":"Govt_job", "Residence_type":"Rural", "smoking_status":"Smokes"
}

response = requests.post("http://127.0.0.1:5000/predict", json=data)

pprint.pprint(response)