from sys import argv
import time
import tweets
# Program that calculates the total number of times each word has been tweeted.
# Author: Jason Keung
# Created: July 4, 2015


if __name__ == "__main__":
    script, infile, outfile = argv
    start_time = time.time()
    print "Starting words_tweeted.py..."
    mytweet = tweets.Tweets(infile, outfile)
    while mytweet.read_tweet():
        mytweet.get_unique_words()
    mytweet.write_dictionary()
    mytweet.close()
    print ("Output is saved to %s ") % (outfile)
    print "words_tweeted.py run successfully!"
    print ("--- %s seconds ---\n") % (time.time() - start_time)
