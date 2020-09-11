from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def get_prediction():
    age = request.args.get('age')
    gender = request.args.get('gender')
    h1 = request.args.get('h1')
    h2 = request.args.get('h2')
    h3 = request.args.get('h3')
    h4 = request.args.get('h4')

	test = np.array([age,gender,h1,h2,h3,h4])
	result = model.evaluate(test, batch_size=1)

	return result
