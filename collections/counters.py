# A Python program to show different ways to create Counter
from collections import Counter

# With sequence of items
print(Counter(['B','B','A','B','C','A','B',
			'B','A','C']))

occurences = Counter(['B','B','A','B','C','A','B', 'B','A','C'])

for char, occurence in occurences.items():
	print(char, occurence)

# with dictionary
print(Counter({'A':3, 'B':5, 'C':2, 'A':4}))

# with keyword arguments
print(Counter(A=3, B=5, C=2))

# Named Parameters / keyword Arguments
def sample(id, name, text='XX'):
	print(id)
	print(name)
	print(text)

sample(1,'ABC')
sample(1,'ABC',text='hello')
sample(text='hello2', id=2, name= 'XYZ')
