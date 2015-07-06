#Module to read in all files from input folder and return a list of tweets.

import os

def inputDirectory(dir):
	folder = sorted(os.listdir(dir))				#Obtains the files that are contained in the input folder and sorts them alphabetically
	array = []										
	for file in folder:
		f = open(dir+file, 'r')						#Opens file for reading only
		for line in f:								#Cycle through all lines/tweets in the file
			array.append(line)						#Adds the line/tweet to the array
		f.close()									#Closes the file
		print "%s sucessfully read" % (file)		#Prints a line to show which file has been successfully read
	return array									#Return an array of strings. Each element in the array is an individual tweet.
