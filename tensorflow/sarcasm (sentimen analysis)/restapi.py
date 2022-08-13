from flask import Flask, request, jsonify, make_response
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import numpy as np
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

# load tokenizer
tokenizer_file = open('tokenizer.pickle', 'rb')
tokenizer = pickle.load(tokenizer_file)

# load model
model = load_model("model.h5")

# parameter
max_length = 120
trunc_type='post'
padding_type='post'

# class dictionary
class_dict = {0 : 'no sarcasm', 1 : 'sarcasm'}

app = Flask(__name__)

# predict model
def predict_label(sentence):
    sentences = []
    sentences.append(sentence)
    sentences_sequences = tokenizer.texts_to_sequences(sentences)
    sentences_padded = pad_sequences(sentences_sequences, padding=padding_type, truncating=trunc_type, maxlen=max_length)
    sentences_padded = np.array(sentences_padded)
    prediction = model.predict(sentences_padded)
    #predicted_bit = np.argmax(model.predict(img_array)) -> softmax
    predicted_bit = np.round(prediction[0][0]).astype('int') # sigmoid
    return class_dict[predicted_bit]

@app.route('/predict', methods=['POST'])
def API():
    # request method using POST
    if request.method == "POST":
        if request.json is None:
            return jsonify({"error": "no data"})
            
        try:
            filejson = request.get_json()
            sentence = str(filejson['sentence'])
            output = predict_label(sentence)
            return make_response(jsonify({"prediction": str(output)}),201)
        except FileNotFoundError as e:
            return make_response(jsonify({"error": str(e)}), 400)
        except Exception as e :
            print (e)
            return make_response(jsonify({"error": str(e)}), 500)

    return "OK"

if __name__ == "__main__":
    app.run(debug=True)