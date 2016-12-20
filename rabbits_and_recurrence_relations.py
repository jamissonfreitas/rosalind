import sys, getopt
import os

def rabbits(month, k):
	if month == 1:
		return 1,0
	
	c, m = rabbits(month-1, k)
	return (k*m), (m + c)
	

def main(argv):
	n = int(argv[0])
	k = int(argv[1])

	print('n=%d k=%d' % (n,k))

	c, m = rabbits(n, k)
	print(c + m)
	
	

if __name__ == "__main__":
	main(sys.argv[1:])	
