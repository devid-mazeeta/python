# Python code to demonstrate namedtuple()
from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple('Student',['name','age','DOB'])
print(Student)

# Adding values
student_obj = Student('Nandini','19','2541997')

# Access using index
print("The Student age using index is : ",end ="")
print(student_obj[1])

# Access using name
print("The Student name using keyname is : ",end ="")
print(student_obj.name)

######################################################################

# Python code to demonstrate namedtuple() and c_make(), _asdict()

######################################################################

# Declaring namedtuple() 
Student = namedtuple('Student',['name','age','DOB'])

# Adding values 
student_obj2 = Student('Nandini','19','2541997')

# initializing iterable  
student_detail = [ 'Manjeet', '19', '411997' ]

# using _make() to return namedtuple()
print("The namedtuple instance using iterable is  : ")
print(student_obj2._make(student_detail))

# using _asdict() to return an OrderedDict()
print("The OrderedDict instance using namedtuple is  : ")
print(student_obj2._asdict())
