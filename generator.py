'''
 File Name: payroll.py
 Author's Name: Tamanna Yasmin Jitu
 Student Number: 300924009
 Date: July 31, 2020
 Description: Showing Data into tabular format
'''

import random

def getWords(filename):
	fp = open(filename)
	temp_list = list()
	for each_line in fp:
		each_line = each_line.strip()
		temp_list.append(each_line)
	words = tuple(temp_list)
	fp.close()
	return words

articles = getWords('articles.txt')
nouns = getWords('nouns.txt')
verbs = getWords('verbs.txt')
prepositions = getWords('prepositions.txt')
conjunctions = getWords('conjunctions.txt')
adjectives = getWords('adjectives.txt')

def sentence():
	return nounPhrase() + " " + verbPhrase()

def nounPhrase():
	prepphrase = " "
	prepchance = random.randrange(100) + 1
	if(prepchance>50):
		prepphrase = " " + adjectivePhrase() + " "
	return random.choice(articles) + prepphrase + random.choice(nouns)

def adjectivePhrase():
	return random.choice(adjectives)

def verbPhrase():
	prepphrase = ""
	prepchance = random.randrange(100) + 1
	if(prepchance>50):
		prepphrase = prepositionalPhrase()
	else:
		prepphrase = conjunctionalPhrase() + " " + verbPhrase()
	return random.choice(verbs) + " " + nounPhrase() + " " + prepphrase
	
def prepositionalPhrase():
	return random.choice(prepositions) + " " + nounPhrase()
	
def conjunctionalPhrase():
	return random.choice(conjunctions) + " " + nounPhrase()

def main():
	number = int(input('Enter number of sentences: '))
	for count in range(number):
		print(sentence())

if __name__=='__main__':
	main()
