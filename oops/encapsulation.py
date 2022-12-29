# Python program to demonstrate private members

# Creating a Base class
class Base:
	def __init__(self):
		self.a = "GeeksforGeeks 1"
		self.__b = "GeeksforGeeks 2"

	def printer(self):
		print(self.__b)
		print(self.c)

# Creating a derived class
class Derived(Base):

	def __init__(self):
		# Calling constructor of Base class
		Base.__init__(self)
		print("Calling public member of base class: ")
		print(self.a)
		print("Calling private member of base class: ")
		print(self.__b)

# Driver code
obj1 = Base()
print(obj1.a) # a is not a private member
# print(obj1.__b) # b is a private member -- AttributeError: 'Base' object has no attribute '__b'
print(obj1.printer)
# print(obj1.printer()) # AttributeError: 'Base' object has no attribute 'c'

# Uncommenting print(obj1.c) will raise an AttributeError
# print(obj1.c) # AttributeError: 'Base' object has no attribute 'c'

# Uncommenting obj2 = Derived() will also raise an AtrributeError as private member of base class is called inside derived class
obj2 = Derived()
