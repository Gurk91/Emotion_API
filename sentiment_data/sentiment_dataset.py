import csv


#keeping just 600 of over 1000 positive lines
with open('positive.txt', 'r') as positive:
	text = positive.read().split('\n')
	relevant_pos = text[:3000]

with open('cleaned_positive.txt', 'w') as cleaned_positive:
	for item in relevant_pos:
		cleaned_positive.write(item + '\n')

#keeping just 600 of over 1000 negative lines
with open('negative.txt', 'r') as negative:
	text = negative.read().split('\n')
	relevant_neg = text[:3000]

with open('cleaned_negative.txt', 'w') as cleaned_negative:
	for item in relevant_neg:
		cleaned_negative.write(item + '\n')


#loading cleaned positives and negatives
with open('cleaned_positive.txt', 'r') as positives:
	pos_text = positives.read().split('\n')

with open('cleaned_negative.txt', 'r') as negatives:
	neg_text = negatives.read().split('\n')


with open('dataset_train.txt', 'w', newline='') as dataset:
	for pos in pos_text[:2399]:
		dataset.write(pos + '\n')
	for neg in neg_text[:2399]:
		dataset.write(neg + '\n')

with open('dataset_test.txt', 'w', newline='') as dataset:
	for pos in pos_text[600:]:
		dataset.write(pos + '\n')
	for neg in neg_text[600:]:
		dataset.write(neg + '\n')









