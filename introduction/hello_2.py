import sys

def print_text(name):
	print("Hello World " + name, end=". ")

# predefined main function
if __name__ == "__main__":
	print_text(sys.argv[1]) # 'sys.argv[]' used to get first command line arguments

print("Welcome to Python")
