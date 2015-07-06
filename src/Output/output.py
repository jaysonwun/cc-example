# Module that write output to a file

def outputStatistics(array, output):
	with open(output, 'w') as f:
		for metric in array:
			f.write(str(metric) + '\n')
	print ("Output is saved to %s") % (output)

def outputWordCount(dictionary, output):
	with open(output, 'w') as f:
	    for key in sorted(dictionary):
	        f.write(key.ljust(28) + str(dictionary[key]) + "\n")
	print ("Output is saved to %s") % (output)
			