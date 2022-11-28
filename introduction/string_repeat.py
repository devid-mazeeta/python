import sys

# user defined function declaration
def variable_repeat(text, nooftimes):
	value = text * nooftimes
	return value

if __name__ == "__main__":
	text = sys.argv[1]
	nooftimes = int(sys.argv[2])
	output = variable_repeat(text, nooftimes)
	print (output)
