import pprint
import requests

data = {
    "sentence":"former versace store clerk sues over secret black code for minority shoppers"
}

response = requests.post("http://127.0.0.1:5000/predict", json=data)

pprint.pprint(response)