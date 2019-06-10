from flask import Flask
import random
from chatbot_logic import predict
from sentiment_analyzer import sentiment
from negative_bot import neg_predict

app = Flask(__name__)


def positive_bot(text):
	result = predict(text)
	return result

def negative_bot(text):
	result = neg_predict(text)
	return result

def cleaner(text):
	assert isinstance(text, str)
	text = text[1:len(text)-1]
	return text


jokes = ["I DECLARE BANKRUPTCY!",
		 "I've been to prison, and well the worst thing about prison was the dementors",
		 "A doctor accidentally prescribes his patient laxatives instead of cough syrup. 3 days later the doctor asks him, 'Are you still coughing?', and he replies, 'I'm too scare too'",
		 "I dreamed I was forced to eat a giant marshmallow. When I woke up, my pillow was gone",
		 "One company owner asks another: 'Tell me, Bill, how come your employees are always on time in the mornings?'. Bill replies: 'Easy. 30 employees and 20 parking spaces'",
		 "Two donkeys are standing at a roadside, one asks the other: So, shall we cross? The other shakes his head: 'No way, look at what happened to the zebra.'",
		 "Why did the physics teacher break up with the biology teacher? There was no chemistry."
		 ]

check1 = '"tell me a joke"'
check2 = '"Tell me a joke"'
check3 = '"i want to laugh"'


@app.route('/')
def intro():
	print("Welcome to ThisBot! Please go to: 'http://0.0.0.0:5008/interactive/ and enter your text following the '/.")
	print("*********************")
	return "Use lower-case letters in your input for best results (this bot isn't the smartest)"

@app.route('/interactive/<text>')
def chatter(text):
	if text == check1 or text == check2 or text == check3:
		return jokes[random.randint(0, len(jokes)-1)]
	polarity = sentiment(text)
	print(polarity)
	if polarity:
		return positive_bot(cleaner(text))
	else:
		return negative_bot(cleaner(text))


if __name__ == '__main__':
	from argparse import ArgumentParser

	parser = ArgumentParser()
	parser.add_argument('-p', '--port', default=5008, type=int, help='port to listen on')
	args = parser.parse_args()
	port = args.port

	app.run(host='0.0.0.0', port=port)