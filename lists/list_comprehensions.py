# to find the cubical value for elements in the list
numbers = [1,2,3,4,5]
cubes = [ num*num*num for num in numbers ]
print (cubes)

# to change the string to upper case and append a additional string
languages = ['java','python','perl']
uppercase = [ langs.upper() + ' language!!!' for langs in languages ]
print (uppercase)

# adding if statement to narrow down the results based on the requirements
# Normal way
marks = [65,45,30,90,35,50,70]
f_marks = []
for mark in marks:
	if mark >= 50:
		f_marks.append(mark)

# Comprehension
marks = [65,45,30,90,35,50,70]
pass_marks = [ m for m in marks if m>=50]
print(pass_marks)
