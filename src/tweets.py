from median_unique import RunningMedian    # for RunningMedian class
# Program that creates a class for tweets
# Author: Jason Keung
# Created: July 4, 2015


class Tweets(object):
    """Defines a class for tweets

        Args:
            infile (str): The input file
            outfile (str): The output file

        Attributes:
            reader (file): The input file
            writer (file): The output file
            tweet (str): List use for storing a tweet
            index (int): The counter for line
            med (RunningMedian): The running median class
            D (dict): The dictionary used for storing unique words_tweeted

    """
    def __init__(self, infile, outfile):

        self.reader = open(infile, 'r')
        self.writer = open(outfile, 'w')
        self.tweet = None
        self.index = 0
        self.med = RunningMedian()
        self.D = {}

    def read_tweet(self):
        """Method to read in a tweet from file

        Returns:
            True if successful, False otherwise.

        """
        self.tweet = self.reader.readline()
        if len(self.tweet) > 0:
            return True
        else:
            return False

    def get_num_unique_words(self):
        """Method to get number of unique words from a tweet

        """
        median = len(set(self.tweet.split()))
        self.med.add(median)
        self.write_median()

    def write_median(self):
        """Method to write a running median to output file

        """
        self.writer.write("{0:.2f} \n".format(self.med.get()))

    def get_words(self):
        """Method to get counts of words from a tweet

        Returns:
            True if successful, False otherwise.

        """
        for word in self.tweet.split():
            if word in self.D:
                self.D[word.lower()] += 1
            else:
                self.D[word.lower()] = 1

    def write_dictionary(self):
        """Method to write word dictionary to file

        """
        for key in sorted(self.D):
            self.writer.write("{}\t{} \n".format(key.ljust(28), self.D[key]))

    def close(self):
        self.writer.close()
