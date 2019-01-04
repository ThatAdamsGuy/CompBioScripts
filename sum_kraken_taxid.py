import sys

dictionary = {}

with open(sys.argv[1]) as f:
	lines = f.readlines()

for line in lines:
	list_of_words = line.split()
	if "taxid" in list_of_words:
		next_word = list_of_words[list_of_words.index("taxid") + 1]
		if next_word in dictionary:
			dictionary[next_word] = dictionary[next_word] + 1
		else:
			dictionary[next_word] = 1

for each in dictionary:
	print each, dictionary[each]
