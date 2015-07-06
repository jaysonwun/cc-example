# Program that will read all tweet files from Input directory, and output the running median for each tweet in the Output directory.

import Input
import Statistics
import Output
from sys import argv

script, directory, output = argv						#Assign arguments

x = Input.inputDirectory(directory)						#Read in input from directory and get list of tweets
y = Statistics.runningMedian(x)							#Run word count and get list of running medians 
Output.outputStatistics(y, output)						#Write list of running medians to file
print ("Output is saved to %s") % (output)
print ("median_unique.py run successfully!")