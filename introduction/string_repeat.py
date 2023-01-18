import sys

# Method 1
character = 'a'
print(character * 8)
number = 1
print(number * 8) # Performs multiplication
print(str(number) * 8) # Performs string repeat

# Method 2
# user defined function declaration
def variable_repeat(text, nooftimes):
	value = text * nooftimes
	return value

if __name__ == "__main__":
	text = sys.argv[1]
	nooftimes = int(sys.argv[2])
	output = variable_repeat(text, nooftimes)
	print(output)
