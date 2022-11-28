import sys

def printtext(name):
	print("Hello World", name, sep=" - ")
	print("Hello World " + name, end=".")

# predefined main function
if __name__ == '__main__':
	printtext("Besant")
	printtext(sys.argv[1]) # 'sys.argv[]' used to get first command line arguments

print("Welcome to Python")
