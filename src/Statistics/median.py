# Module that calculates the median number of unique words per tweet.

#Helper method to get median of an array
def getMedian(array):
	array = sorted(array)
	if len(array)==0:												#Returns Empty List if length is 0
		return "Empty List"
	elif len(array)%2==1:											#If list has odd number of elements return the middle number
		return array[len(array)/2]
	elif len(array)%2==0:											#If list has even number of elements average the two middle numbers
		return (array[len(array)/2-1]+array[len(array)/2]) / 2.0

#Method to create a list of running medians from a list of tweets
def runningMedian(array):
	numberUniquePerTweet = []										#Initialize list of number of unique words per tweet
	runningMedian = []												#Initialize list of running medians
	for sentence in array:
		words = sentence.split()									#Split each tweet into a list of individual words
		numberUniquePerTweet.append(len(list(set(words))))			#Add the length of the number of unique words to numberUniquePerTweet
		runningMedian.append(getMedian(numberUniquePerTweet))		#Add the running median to the runningMedian list
	return runningMedian