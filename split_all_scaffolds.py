#USAGE: python split_all_scaffolds.py <INPUT_FILE> <OUTPUT_DIRECTORY_NAME>
#As per usual, incorrect usage will crash.

import sys
import os

if not os.path.exists(sys.argv[2]):
	os.makedirs(sys.argv[2])

cur_path = os.path.dirname(__file__)
with open(sys.argv[1]) as fastaFile:
	for line in fastaFile:
		if line[0] == '>':
			newLine = line.rstrip()
			new_path = os.path.join(os.getcwd(), sys.argv[2] + "/" + newLine[1:] + ".fa") 
			f = open(new_path, "w+")
		f.write(line)
