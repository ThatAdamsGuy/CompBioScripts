#USAGE - python fasta_million_character_split.py <INPUT_FILE> <DIRECTORY_NAME>
#File will just crash if not used otherwise, did not use validation. Sorry.

import sys
import os

total_count = 0
file_count = 0

string_list = []

if not os.path.exists(sys.argv[2]):
	os.makedirs(sys.argv[2])

cur_path = os.path.dirname(__file__)

with open(sys.argv[1]) as fastaFile:
	for line in fastaFile:
		if line[0] == '>':
			if total_count > 900000:
				print("IN IF")
				new_path = os.path.join(os.getcwd(), sys.argv[2] + "/" + sys.argv[2] + "_" + str(file_count) + ".fa") 
				f = open(new_path, "w+")
				for string in string_list:
					f.write(string)
				f.close()
				del string_list[:]
				total_count = 0
				file_count += 1	
		string_list.append(line)
		total_count += len(line)

	if string_list:
		new_path = os.path.join(os.getcwd(), sys.argv[2] + "/" + sys.argv[2] + "_last.fa") 
		f = open(new_path, "w+")
		for string in string_list:
			f.write(string)
		f.close()
