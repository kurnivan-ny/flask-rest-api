import pprint
import requests

data = {"age":20, "bmi":30, "smoker":"yes", "gender":"male"}

response = requests.post("http://127.0.0.1:5000/predict", json=data)

pprint.pprint(response)