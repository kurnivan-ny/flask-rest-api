from flask import Flask, request, jsonify, make_response
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow import expand_dims
import numpy as np
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

# load model
model = load_model("model.h5")

# class dictionary
class_dict = {0 : 'Heart', 1 : 'Oblong', 2 : 'Oval', 3 : 'Round', 4 : 'Square'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './testing/'

# predict model
def predict_label(img_path):
    loaded_img = load_img(img_path, target_size=(224,224,3))
    img_array = img_to_array(loaded_img)/255. # normalisasi
    img_array = expand_dims(img_array, 0)
    predicted_bit = np.argmax(model.predict(img_array)) #softmax
    #predicted_bit = np.round(model.predict(img_array)[0][0]).astype('int') -> sigmoid
    return class_dict[predicted_bit]

@app.route('/predict', methods=['POST'])
def API():
    # request method using POST
    if request.method == "POST":
        if request.json is None:
            return jsonify({"error": "no data"})
            
        try:
            filejson = request.get_json()
            imageName = filejson['image']
            img_path = os.path.join(app.config['UPLOAD_FOLDER'], imageName)
            output = predict_label(img_path)
            return make_response(jsonify({"prediction face": str(output)}),201)
        except FileNotFoundError as e:
            return make_response(jsonify({"error": str(e)}), 400)
        except Exception as e :
            print (e)
            return make_response(jsonify({"error": str(e)}), 500)

    return "OK"

if __name__ == "__main__":
    app.run(debug=True)