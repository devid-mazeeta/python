# defining class
class StudentData:

	# class variables
	college = "Karpaga Vinayaga College of Engineering and Technology"
	location = "Madurantakam"

    # constructor method with instance variable [must have 'self' keyword as first parameter]
	def __init__(self, name, age):
		# instance variables
		self.name1 = name
		self.age = age

	# normal method with instance variable percentage
	def studentpercentage(self, percentage):
		print("This student has got " + str(percentage) + "% of marks in UG")

# defining method
def student_data():

	# first object, setting up instance variables of constructor method
	student1 = StudentData("Devid", 23)

	# print out instance variable - 'name' & 'age' of first object
	print(student1.name1)
	print(student1.age)

	# print out class variable - 'college' & 'location' of first object
	print(student1.college)
	print(student1.location)

	# second object, setting up instance variables of constructor method
	student2 = StudentData("Loki", 22)

	# print out instance variable - 'name' & 'age' of second object
	print(student2.name1)
	print(student2.age)
	print(student1.age)

	# print out class variable - 'college' & 'location' of second object
	print(student2.college)
	print(student2.location)

	# passing instance variable('percentage') to method ('studentPercentage')
	student1.studentpercentage(90)
	student2.studentpercentage(80)

if __name__ == "__main__":
    student_data()
