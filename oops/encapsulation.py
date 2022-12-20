# Python program to demonstrate private members

# Creating a Base class
class Base:
	def __init__(self):
		self.a = "GeeksforGeeks 1"
		self.__c = "GeeksforGeeks 2"
	
	def printer(self):
		print(self.c)

# Creating a derived class
class Derived(Base):
	def __init__(self):

		# Calling constructor of Base class
		Base.__init__(self)
		print("Calling private member of base class: ")
		print(self.__c)

# Driver code
obj1 = Base()
print(obj1.a) # a is not a private member
print(obj1.printer)

# Uncommenting print(obj1.c) will raise an AttributeError
# print(obj1.c)

# Uncommenting obj2 = Derived() will also raise an AtrributeError as private member of base class is called inside derived class
# obj2 = Derived()