from textblob import TextBlob


with open('movie_lines.txt', encoding='ISO-8859-1') as file:
	raw = file.read().split('\n')


filtered = raw[:40000]

#removing '+++$+++'
test = filtered[:2]
#print(test)
blob = TextBlob(test[1])
#print(blob.words)

def cleaner(text_list):
	output = []
	for item in text_list:
		blob = TextBlob(item)
		output.append(blob.words[4:])
	return output

initialized = cleaner(filtered)

def joiner(text_list):
	output = []
	for item in text_list:
		sentence = ' '.join(item)
		output.append(sentence)
	return output

cleaned = joiner(initialized)


with open('movie_cleaned.txt', 'w') as file:
	for item in cleaned:
		file.write(str(item) + '\n')
