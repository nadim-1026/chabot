from chatbot import get_response,get_response2
from flask import Flask, render_template, request


app = Flask(__name__)



@app.route('/')
def home():
	return render_template('index.html')


@app.route('/get')
def getMessage():
	message = request.args.get('msg')
	response1 = get_response(message)
	response2 = get_response2(message)

	return response1+'<br>'+response2

# main driver function
if __name__ == '__main__':
	app.run()
