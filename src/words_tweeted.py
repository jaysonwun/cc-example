# Program that will read all tweet files from Input directory, and output the count of the words in the Output directory.

import Input
import Statistics
import Output
from sys import argv

script, directory, output = argv					#Assign arguments

x = Input.inputDirectory(directory)					#Read in input from directory and get list of tweets
y = Statistics.wordCount(x)							#Run word count and get dictionary of words 
#y = Statistics.wordCount(x,".?,;"					#ADDITIONAL FEATURE: add additional paramater to filter character(s) from tweets
Output.outputWordCount(y, output)					#Write dictionary of words to file
print ("words_tweeted.py run successfully!")
