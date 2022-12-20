class Dog:

	# class attribute
	attr1 = "mammal"

	# Instance attribute
	def __init__(self, name):
		self.newname = name

	def speak(self):
		print("My name is {}".format(self.newname))

# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is a {1} {0}".format(Rodger.__class__.attr1,"Animal"))
print("Tommy is also a {} {}".format(Tommy.attr1,"Animal"))

# Accessing instance attributes
print("My name is {}".format(Rodger.newname))
print("My name is {}".format(Tommy.newname))

# Accessing class methods
Rodger.speak()
Tommy.speak()
