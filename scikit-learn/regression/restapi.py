from flask import Flask, request, jsonify, make_response
import pickle

# load model
model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='btyes')

# numerical mean and std after standardize
numerical_mean = [39.23802395209581, 30.65882110778443]
numerical_std = [14.03757153211609, 6.1004017162649875]

# target mean and std after standardize
target_mean = 13279.121486655948
target_std = 12110.359656344175

app = Flask(__name__)

# get values from json (dictionary)
def getvalues(filejson):
    values = []
    values.append(filejson["age"])
    values.append(filejson["bmi"])
    values.append(filejson["smoker"])
    values.append(filejson["gender"])
    return values

# preprocessing input data before training (standardize)
def preprocessing(filejson):
    data = []
    age, bmi, smoker, gender = getvalues(filejson)

    data.append((age-numerical_mean[0])/numerical_std[0])
    data.append((bmi-numerical_mean[1])/numerical_std[1])

    if smoker.lower() == 'no':
        data.extend([1,0])
    else:
        data.extend([0,1])

    if gender.lower() == 'female':
        data.extend([1,0])
    else:
        data.extend([0,1])
    return data

# predict model
def predict(filejson):
    data = preprocessing(filejson)
    prediction = model.predict([data])
    output = round((prediction[0]* target_std) + target_mean, 2) # return value after standardize
    return output

@app.route('/predict', methods=['POST'])
def API():
    # request method using POST
    if request.method == "POST":
        if request.json is None:
            return jsonify({"error": "no data"})
            
        try:
            output = predict(request.get_json())
            return make_response(jsonify({"prediction": float(output)}),201)
        except FileNotFoundError as e:
            return make_response(jsonify({"error": str(e)}), 400)
        except Exception as e :
            print (e)
            return make_response(jsonify({"error": str(e)}), 500)

    return "OK"

if __name__ == "__main__":
    app.run(debug=True)