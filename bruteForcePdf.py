#! python3
# bruteForcePdf.py - Brute force guesses
# password to specified PDF in argument.

import sys, PyPDF2

# Cycle through dictionary until successful decryption.
def search_dictionary(filename):

	pdfFile = open(filename, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFile)

	dictionaryFile = open('dictionary.txt')
	dictionary = dictionaryFile.readlines()

	for entry in dictionary:

		# Clean the entry.
		entry = entry.replace('\n','')

		# Create switch for breaking out of search.
		isFound = False

		# Note that entry comes in uppercase as default.
		if (pdfReader.decrypt(entry)):
			isFound = True

		# Also try entry as lowercase.
		elif (pdfReader.decrypt(entry.lower())):
			entry = entry.lower()
			isFound = True
		
		# Present password and break search once found.
		if isFound:
			print('Password is: %s' % entry)
			dictionaryFile.close()
			pdfFile.close()
			return

try:
	search_dictionary(sys.argv[1])
	
except:
	print('Please give a valid .pdf in argument.')