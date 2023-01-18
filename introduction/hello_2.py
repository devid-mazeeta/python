import sys

def printtext(name):
	print("Hello World", name, sep=" - ")
	print("Hello World " + name, end=".")

# predefined main function
if __name__ == '__main__':
	printtext("Besant")
	commandlineip1 = sys.argv[1]
	printtext(commandlineip1) # 'sys.argv[1]' used to get first command line arguments
	printtext(sys.argv[2]) # 'sys.argv[2]' used to get second command line arguments

print("Welcome to Python")
