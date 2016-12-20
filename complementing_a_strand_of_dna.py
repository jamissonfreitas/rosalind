import sys, getopt
import os

def main(argv):
	inputFile = argv[0]
	outputFile = '%s_answer' % (os.path.basename(inputFile))

	out = open(outputFile, 'w')
	f = open(inputFile)

	seq = f.read().upper()[::-1]

	print(seq)
	
	answer = ''
	for c in seq:
		if c == 'A':
			answer += 'T'
		elif c == 'T':
			answer += 'A'
		elif c == 'C':
			answer += 'G'
		elif c == 'G':
			answer += 'C'
		else:
			print('erro')
		

	print(answer)
	out.write(answer)

if __name__ == "__main__":
	main(sys.argv[1:])	
