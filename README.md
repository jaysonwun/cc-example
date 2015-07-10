Insight Data Engineering - Coding Challenge
===========================================================

## Challenge Summary

This challenge is to implement two features:

1. Calculate the total number of times each word has been tweeted.
2. Calculate the median number of *unique* words per tweet, and update this median as tweets come in. 

For example, suppose the following three tweets come in, one after the other

- is #bigdata finally the answer to end poverty? @lavanyarathnam http://ow.ly/o8gt3  #analytics  
- interview: xia wang, astrazeneca on #bigdata and the promise of effective healthcare #kdn http://ow.ly/ot2uj  
- big data is not just for big business. on how #bigdata is being deployed for small businesses: http://bddy.me/1bzukb3  @cxotodayalerts #smb  

The first feature would produce the following total count for each word:

	#analytics  				1
	#bigdata 					3
	#kdn 						1
	#smb 						1
	@cxotodayalerts 			1
	@lavanyarathnam 			1
	and 						1
	answer  					1
	astrazeneca 				1
	being 						1
	big 						2
	business. 					1 
	businesses: 				1
	data 						1
	deployed 					1
	effective 					1
	end 						1
	finally 					1
	for 						2
	healthcare 					1
	how 						1
	http://bddy.me/1bzukb3  	1
	http://ow.ly/o8gt3 	 		1
	http://ow.ly/ot2uj  		1
	interview: 					1
	is  						3
	just 						1
	not 						1
	of 							1
	on 							2
	poverty? 					1
	promise 					1
	small 						1
	the  						2
	to  						1
	wang,						1
	xia 						1

Note that the output of the first feature is outputted in order, according to the [ASCII Code](http://www.ascii-code.com).   

For the second feature, the number of unique words in each tweet is 11, 14, and 17 (since the words 'is', 'big', and 'for' appear twice in the third tweet).  This means that the set of unique words per tweet is {11} after the first tweet arrives, is {11, 14} after the second tweet arrives, and is {11, 14, 17} after all three tweets arrive.  The output of the running median will display as a double with only 2 digits after the decimal.  Thus, the second feature would produce the following output:

	11.00
	12.50
	14.00

## Assumptions

- Each tweet only contains lowercase letters, numbers, and ASCII characters like ':', '@', and '#'.
- A word is defined as anything separated by whitespace. 
- The 'tweets.txt' input file will only contain lowercase letters, numbers, and ASCII characters (e.g. common punctuation and characters like '@', and '#').
- 'tweets.txt' will have the content of each tweet on a newline.
- 'tweets.txt' will have no missing lines between tweets

## Sample Input

./tweet_input/tweets.txt:

	Contents of first tweet  
	Contents of second tweet  
	Contents of third tweet  
	.
	.
	.
	Contents of last tweet  

## Python Libraries Used
	
	- sys
	- heapq
	- time

## Instructions

### Checkout Code

	$ git clone https://github.com/jaysonwun/cc-example.git

### Run words_tweeted.py and median_unique.py From Root Directory 

Linux: 

	$ ./run.sh

Mac:

	$ ./run.sh

### Alternatively: Run words_tweeted.py and median_unique.py from /src directory

Linux:

	$ python words_tweeted.py ../tweet_input/tweets.txt ../tweet_output/ft1.txt
	$ python median_unique.py ../tweet_input/tweets.txt ../tweet_output/ft2.txt

Mac:

	$ python words_tweeted.py ../tweet_input/tweets.txt ../tweet_output/ft1.txt
	$ python median_unique.py ../tweet_input/tweets.txt ../tweet_output/ft2.txt

Output will be saved to the ./tweet_output/ directory
