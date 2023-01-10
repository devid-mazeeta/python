# Python program to demonstrate userlist
from collections import UserList

# Creating a List where deletion is not allowed
class MyList(UserList):

	# Function to stop deletion from List
	def remove(self, s = None):
		raise RuntimeError("Deletion not allowed")

	# Function to stop pop from List
	def pop(self, s = None):
		raise RuntimeError("Deletion not allowed")

# Driver's code
user_list_obj = MyList([1, 2, 3, 4])

print("Original List")
print(user_list_obj)

# Inserting to List
user_list_obj.append(5)
print("After Insertion")
print(user_list_obj)

# Deleting From List
user_list_obj.remove(s='q')
