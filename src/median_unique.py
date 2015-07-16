from sys import argv    # for passing arguments from command line
import time             # for tracking time
import tweets           # contains Tweets class
# Program that calculates the median number of unique words per tweet
# Author: Jason Keung
# Created: July 4, 2015


if __name__ == "__main__":
    script, infile, outfile = argv
    start_time = time.time()
    print ("Starting median_unique.py...")
    mytweet = tweets.Tweets(infile, outfile)
    while mytweet.read_tweet():
        mytweet.get_num_unique_words()
        mytweet.write_median()    # write median after EACH line is read
    mytweet.close()
    print ("Output is saved to %s ") % (outfile)
    print ("median_unique.py run successfully!")
    print ("--- %s seconds ---\n") % (time.time() - start_time)
