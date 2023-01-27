# To find the cubical value for elements in the list
# Without list comprehension
numbers = [1,2,3,4,5]
cubes = []
for num in numbers:
	cubes.append(num*num*num) # cubes.append(num**3)
print(cubes)

# With list comprehension
cubes = [ num**3 for num in numbers ]
print(cubes)

# To change the string to upper case and append a additional string
# Without list comprehension
languages = ['java','python','perl']
uppercaselangs = []
for language in languages:
	uppercaselangs.append(language.upper() + ' language!!!')
print(uppercaselangs)

# With list comprehension
uppercaselangs = [ language.upper() + ' language!!!' for language in languages ]
print(uppercaselangs)

# Adding if statement to narrow down the results based on the requirements
# Example 1
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

# Example 2
# Without list comprehension
fivedivisibles = []
for num in range(100,201):
	if num % 5 == 0:
		fivedivisibles.append(num)
print(fivedivisibles)

# With list comprehension
fivedivisibles = [ num for num in range(100,201) if num % 5 == 0 ]
print(fivedivisibles)
