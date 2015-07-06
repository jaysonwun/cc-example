# Module that calculates the total number of times each word has been tweeted.
from collections import OrderedDict
import string

#Method to create a dictionary of words and counts from a list of tweets
def wordCount(array, exclude=""):
	D = dict()
	for sentence in array:
		words = sentence.split()									   #Separates the sentence into an array of words.
		for word in words:
			word = word.translate(string.maketrans("",""), exclude)    #ADDITIONAL FEATURE: Filters characters from each word. Varible "exclude" contains characters to remove.
			if word in D:
				D[word.lower()]+=1									   #Adds 1 to the count of the lowercased word in the dictionary if word exists
			else:
				D[word.lower()]=1									   #Sets count = 1 and creates a key in the dictionary if word doesn't exist
	sortedD = OrderedDict(sorted(D.items()))						   #Creates an ordered dictionary that keeps the words in alphabetical order
	return sortedD

