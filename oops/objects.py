class Dog:

	# class attribute
	attr1 = "mammal"

	def __init__(self, name):
		self.newname = name # Instance attribute

	def speak(self):
		print("My name is {}".format(self.newname))

# Object instantiation
rodger = Dog("Rodger")
tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is a {1} {0}".format(rodger.__class__.attr1,"Animal"))
print("Tommy is also a {} {}".format(tommy.attr1,"Animal"))

# Accessing instance attributes
print("My name is {}".format(rodger.newname))
print("My name is {}".format(tommy.newname))

# Accessing class methods
rodger.speak()
tommy.speak()
