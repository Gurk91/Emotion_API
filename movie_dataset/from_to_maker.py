

with open('movie_cleaned.txt', 'r') as file:
	data = file.read().split('\n')

with open('from.txt', 'w') as dial:
	for item in data[::2]:
		dial.write(item + '\n')

with open('to.txt', 'w') as to:
	for item in data[1::2]:
		to.write(item + '\n')


