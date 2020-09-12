from flask import Flask
from flask import request
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


app = Flask(__name__)
model = keras.models.load_model('./model.h5')

@app.route('/predict')
def get_prediction():
    # TODO: Consider using post method instead of get
    age = request.args.get('age')
    gender = request.args.get('gender')
    h1 = request.args.get('h1')
    h2 = request.args.get('h2')
    h3 = request.args.get('h3')
    h4 = request.args.get('h4')

    # test = np.array([age,gender,h1,h2,h3,h4])
    test = np.array([[int(age),int(gender),int(h1),int(h2),int(h3),int(h4)]])
    result = model.predict_classes(test, batch_size=1)[0]
    return str(result)

if __name__ == '__main__':
    app.run()
