# Python code to demonstrate namedtuple()
from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple('Student',['name','age','DOB'])
print(Student)

# Adding values
S = Student('Nandini','19','2541997')

# Access using index
print("The Student age using index is : ",end ="")
print(S[1])

# Access using name
print("The Student name using keyname is : ",end ="")
print(S.name)
# Python code to demonstrate namedtuple()
from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple('Student',['name','age','DOB'])
print(Student)

# Adding values
S = Student('Nandini','19','2541997')

# Access using index
print("The Student age using index is : ",end ="")
print(S[1])

# Access using name
print("The Student name using keyname is : ",end ="")
print(S.name)

######################################################################

# Python code to demonstrate namedtuple() and c_make(), _asdict()
from collections import namedtuple

# Declaring namedtuple() 
Student = namedtuple('Student',['name','age','DOB'])

# Adding values 
S = Student('Nandini','19','2541997')

# initializing iterable  
li = ['Manjeet', '19', '411997' ]

# using _make() to return namedtuple()
print("The namedtuple instance using iterable is  : ")
print(Student._make(li))

# using _asdict() to return an OrderedDict()
print("The OrderedDict instance using namedtuple is  : ")
print(S._asdict())
