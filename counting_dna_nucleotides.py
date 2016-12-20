import sys, getopt
import os

def main(argv):
	inputFile = argv[0]
	outputFile = '%s_answer' % (os.path.basename(inputFile))

	out = open(outputFile, 'w')
	f = open(inputFile)

	seq = f.read().upper()
	
	answer = '%d %d %d %d' % (seq.count('A'),
				  seq.count('C'),
				  seq.count('G'),
				  seq.count('T'))
	print(answer)
	out.write(answer)

if __name__ == "__main__":
	main(sys.argv[1:])	
