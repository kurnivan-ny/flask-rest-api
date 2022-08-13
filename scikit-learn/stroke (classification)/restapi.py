from flask import Flask, request, jsonify, make_response
import pickle

# load model
model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='btyes')

# numerical mean and std after standardize
numerical_mean = [49.38725052129878, 108.44428358653559, 30.439529341674113]
numerical_std = [18.31051345420408, 47.92139198493866, 7.249737664407547]

# class dictionary
class_dict = {0: 'no', 1: 'yes'}

app = Flask(__name__)

# get values from json (dictionary)
def getvalues(filejson):
    values = []
    values.append(filejson["age"])
    values.append(filejson["avg_glucose_level"])
    values.append(filejson["bmi"])
    values.append(filejson["gender"])
    values.append(filejson["hypertension"])
    values.append(filejson["heart_disease"])
    values.append(filejson["ever_married"])
    values.append(filejson["work_type"])
    values.append(filejson["Residence_type"])
    values.append(filejson["smoking_status"])
    return values

# preprocessing input data before training (standardize)
def preprocessing(filejson):
    data = []
    age, avg_glucose_level, bmi, gender, hypertension, heart_disease, ever_married, work_type, Residence_type, smoking_status = getvalues(filejson)

    data.append((age-numerical_mean[0])/numerical_std[0])
    data.append((avg_glucose_level-numerical_mean[1])/numerical_std[1])
    data.append((bmi-numerical_mean[2])/numerical_std[2])

    if gender.lower() == 'female':
      data.extend([1,0])
    else:
      data.extend([0,1])

    if hypertension.lower() == 'no':
      data.extend([1,0])
    else:
      data.extend([0,1])

    if heart_disease.lower() == 'no':
      data.extend([1,0])
    else:
      data.extend([0,1])

    if ever_married.lower() == 'no':
      data.extend([1,0])
    else:
      data.extend([0,1])
      
    if work_type.lower() == 'govt_job':
      data.extend([1,0,0,0])
    elif work_type.lower() == 'never_worked':
      data.extend([0,1,0,0])
    elif work_type.lower() == 'private':
      data.extend([0,0,1,0])
    elif work_type.lower() == 'self-employed':
      data.extend([0,0,0,1])

    if Residence_type.lower() == 'rural':
      data.extend([1,0])
    else:
      data.extend([0,1])

    if smoking_status.lower() == 'formerly smoked':
      data.extend([1,0,0])
    elif smoking_status.lower() == 'never smoked':
      data.extend([0,1,0])
    elif smoking_status.lower() == 'smokes':
      data.extend([0,0,1])
    return data

# predict model
def predict(filejson):
    data = preprocessing(filejson)
    prediction = model.predict([data])
    return class_dict[prediction[0]]

@app.route('/predict', methods=['POST'])
def API():
    # request method using POST
    if request.method == "POST":
        if request.json is None:
            return jsonify({"error": "no data"})
            
        try:
            output = predict(request.get_json())
            return make_response(jsonify({"prediction": str(output)}),201)
        except FileNotFoundError as e:
            return make_response(jsonify({"error": str(e)}), 400)
        except Exception as e :
            print (e)
            return make_response(jsonify({"error": str(e)}), 500)

    return "OK"

if __name__ == "__main__":
    app.run(debug=True)