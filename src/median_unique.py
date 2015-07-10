from sys import argv    # for passing arguments from command line
import heapq as hq      # for process heaps
import time             # for tracking time
import tweets           # contains Tweets class
# Program that calculates the median number of unique words per tweet
# Author: Jason Keung
# Created: July 4, 2015


class RunningMedian(object):
    """Defines a class for tweets

        Attributes:
            minheap (list): The min heap that will contain the higher numbers.
            maxheap (list): The max heap that will contain the lower numbers.
            index (int): The index to track line number.
            condition (str): Condition that will specify which heap has more
                elements. Possible condition values include: even, maxplus1,
                maxgreater, minplus1, or mingreater.

    """

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        self.index = 0
        self.condition = "even"

    def add(self, val):
        """Method to add a running median to minheap or maxheap. Initializes
        minheap to larger of first two numbers. Intializes maxheap to the
        smaller of the first two numbers. The follow the following algorithm:

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

        if self.index == 0:
            # add first value to both heaps
            hq.heappush(self.minheap, val)
            hq.heappush(self.maxheap, -1 * val)

        elif self.index == 1:
            # add second value to both heaps
            hq.heappush(self.minheap, val)
            hq.heappush(self.maxheap, -1 * val)
            # keep the smallest value in maxheap and largest value in minheap
            self.maxheap = hq.nlargest(1, self.maxheap)
            self.minheap = hq.nlargest(1, self.minheap)

        else:
            # add next item to one of the heaps
            if val < -1 * self.maxheap[0] and self.condition == "even":
                hq.heappush(self.maxheap, -1 * val)
                self.condition = "maxplus1"
            elif val < -1 * self.maxheap[0] and self.condition == "maxplus1":
                hq.heappush(self.maxheap, -1 * val)
                self.condition = "maxgreater"
            elif val >= -1 * self.maxheap[0] and self.condition == "even":
                hq.heappush(self.minheap, val)
                self.condition = "minplus1"
            elif val >= -1 * self.maxheap[0] and self.condition == "minplus1":
                hq.heappush(self.minheap, val)
                self.condition = "mingreater"
            else:
                pass

            # now balance the heaps
            if self.condition == "maxgreater":
                hq.heappush(self.minheap, -1 * hq.heappop(self.maxheap))
                self.condition = "even"
            elif self.condition == "mingreater":
                hq.heappush(self.maxheap, -1 * hq.heappop(self.minheap))
                self.condition = "even"
            else:
                pass

            # only keep 3 values stored in the heap for memory purposes
            self.maxheap = hq.nsmallest(3, self.maxheap)
            self.minheap = hq.nsmallest(3, self.minheap)
        self.index += 1

    def get(self):
        """Method to calculate median based on condition, maxheap, and minheap.
        if the heaps contain equal elements;
        median = (root of maxHeap + root of minHeap)/2
        else
        median = root of the heap with more elements
        (http://stackoverflow.com/questions/10657503/find-running-median-from-a-stream-of-integers)

        Returns:
            float

        """

        if self.condition == "even":
            return (-1 * min(self.maxheap) + min(self.minheap)) / 2.
        elif self.condition == "maxplus1":
            return -1 * min(self.maxheap)
        elif self.condition == "minplus1":
            return min(self.minheap)
        else:
            pass


if __name__ == "__main__":
    script, infile, outfile = argv
    start_time = time.time()
    mytweet = tweets.Tweets(infile, outfile)
    print ("Starting median_unique.py...")
    while mytweet.read_tweet():
        mytweet.get_unique_words()
    mytweet.close()
    print ("Output is saved to %s ") % (outfile)
    print ("median_unique.py run successfully!")
    print ("--- %s seconds ---*\n") % (time.time() - start_time)
