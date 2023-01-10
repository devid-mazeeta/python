# Python program to demonstrate userdict
from collections import UserDict

# Creating a Dictionary where deletion is not allowed
class MyDict(UserDict):

	def __init__(self, dict):
		self.print_text = "Deletion not allowed"

	# Function to stop deletion from dictionary
	def __del__(self):
		raise RuntimeError(self.print_text)

	# Function to stop pop from dictionary
	def pop(self, s = None):
		raise RuntimeError(self.print_text)

	# Function to stop popitem from Dictionary
	def popitem(self, s = None):
		raise RuntimeError(self.print_text)

# Driver's code
user_dict_obj = MyDict({
	'a':1,
	'b': 2,
	'c': 3
})

user_dict_obj.pop(1)
