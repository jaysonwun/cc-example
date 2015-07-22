import heapq as hq      # for process heaps
# Program that creates a class for Tweets and RunningMedian
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
            med (RunningMedian): The running median class
            D (dict): The dictionary used for storing unique words_tweeted

    """
    def __init__(self, infile, outfile):

        self.reader = open(infile, 'r')
        self.writer = open(outfile, 'w')
        self.tweet = None
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

    def get_unique_words(self):
        """Method to get counts of unique words from a tweet

        """
        for word in self.tweet.split():
            if word in self.D:
                self.D[word.lower()] += 1
            else:
                self.D[word.lower()] = 1

    def write_median(self):
        """Method to write a running median to output file

        """
        self.writer.write("{0:.1f} \n".format(self.med.get()))

    def write_dictionary(self):
        """Method to write word dictionary to file

        """
        for key in sorted(self.D):
            self.writer.write("{}\t{} \n".format(key.ljust(28), self.D[key]))

    def close(self):
        self.writer.close()


class RunningMedian(object):
    """Defines a class for RunningMedian

        Attributes:
            minheap (list): The min heap that will contain the higher numbers.
            maxheap (list): The max heap that will contain the lower numbers.
            even (boolean): Condition that will specify which heap has more
                elements. 

    """

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self.even = True

    def add(self, val):
        """Method to add a running median to minheap or maxheap. Initializes
        minheap to larger of first two numbers. Intializes maxheap to the
        smaller of the first two numbers. A maxheap will be represented by
        negative numbers. The following algorithm will be used:

        Step 1: Add next item to one of the heaps
        if next item is smaller than maxHeap root add it to maxHeap,
        else add it to minHeap

        Step 2: Balance the heaps (after this step heaps will be either
        balanced or one of them will contain 1 more item)
        if number of elements in one of the heaps is greater than the other by
        more than 1, remove the root element from the one containing more
        elements and add to the other one
        (http://stackoverflow.com/questions/10657503/find-running-median-from-a-stream-of-integers)

        Args:
            val (int): Median to be added to the heap.

        """

        if self.even:
            # to intiailize if maxheap is empty
            if not self.maxheap:
                hq.heappush(self.maxheap, val * -1)
            # push to minheap and then allow maxheap to have more elements
            elif val > self.maxheap[0] * -1:
                x = hq.heappushpop(self.minheap, val)
                hq.heappush(self.maxheap, x * -1)
            # just push to maxheap
            else:
                hq.heappush(self.maxheap, val * -1)
            # set even condition to False, maxheap has 1 additional element
            self.even = False

        else:
            # push to minheap
            if val > self.maxheap[0] * -1:
                hq.heappush(self.minheap, val)
            # push to maxheap then balance to minheap
            else:
                x = hq.heappushpop(self.maxheap, val * -1)
                hq.heappush(self.minheap, x * -1)
            # maxheap has same number elements as minheap
            self.even = True
        # only keep 3 values stored in the heap for memory purposes
        self.maxheap = hq.nsmallest(3, self.maxheap)
        self.minheap = hq.nsmallest(3, self.minheap)

    def get(self):
        """Method to calculate median based on "even" condition.
        if the heaps contain equal elements;
        median = (root of maxHeap + root of minHeap)/2
        else
        median = root of the heap with more elements
        (http://stackoverflow.com/questions/10657503/find-running-median-from-a-stream-of-integers)

        Returns:
            float

        """

        if self.even:
            return (min(self.maxheap) * -1 + min(self.minheap)) / 2.
        else:
            return min(self.maxheap) * -1
