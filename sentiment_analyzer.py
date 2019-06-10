from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB

#Performs sentiment_analysis using NaiveBayes

with open('dataset_train.txt', 'r') as file:
	data = file.read().split('\n')

def label_process_train(data):
	output = []
	for item in data[:2399]: #first 2399 are positive
		output.append([item, 1])
	for item in data[2399:]: #last 2399 are negative
		output.append([item, 0])
	return output

labelled_train = label_process_train(data)

with open('dataset_test.txt', 'r') as file:
	test = file.read().split('\n')

def label_process_test(data):
	output = []
	for item in data[:600]: #first 600 are positive
		output.append([item, 1])
	for item in data[600:]: #last 600 are negative
		output.append([item, 0])
	return output 

labelled_test = label_process_test(test)

def training_step(data, vectorizer):
    training_text = [data[0] for data in data]
    training_result = [data[1] for data in data]

    training_text = vectorizer.fit_transform(training_text)

    return BernoulliNB().fit(training_text, training_result)

vectorizer = CountVectorizer(binary='true') #vectorizes the input text into numbers
classifier = training_step(labelled_train, vectorizer)

def sentiment(text):
	return classifier.predict(vectorizer.transform([text]))[0]












