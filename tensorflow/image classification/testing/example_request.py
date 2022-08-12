import pprint
import requests

data = {
    "image":"round face.jpg"
}

response = requests.post("http://127.0.0.1:5000/predict", json=data)

pprint.pprint(response)