# to find the cubical value for elements in the list
# Without list comprehension
cubes = []
for num in numbers:
	cubes.append(num*num*num)
print(cubes)

# With list comprehension
numbers = [1,2,3,4,5]
cubes = [ num*num*num for num in numbers ]
print (cubes)

# to change the string to upper case and append a additional string
# Without list comprehension
uppercase = []
for langs in languages:
	uppercase.append(langs.upper() + ' language!!!')
print(uppercase)

# With list comprehension
languages = ['java','python','perl']
uppercase = [ langs.upper() + ' language!!!' for langs in languages ]
print (uppercase)

# adding if statement to narrow down the results based on the requirements
# Without list comprehension
marks = [65,45,30,90,35,50,70]
pass_marks = []
for mark in marks:
	if mark >= 50:
		pass_marks.append(mark)
print(pass_marks)

# With list comprehension
marks = [65,45,30,90,35,50,70]
pass_marks = [ m for m in marks if m>=50]
print(pass_marks)
