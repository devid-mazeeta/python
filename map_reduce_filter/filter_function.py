# filter(func, iter)

# function filters vowels
def vowels(letter):
	letters = ['a', 'e', 'i', 'o', 'u']
	if (letter in letters):
		return True
	else:
		return False

# sequence
characters = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(vowels, characters)

print('The filtered letters are:')
for char in filtered:
	print(char)

# a list contains both even and odd numbers.
mylist = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, mylist)
print(list(result))

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, mylist)
print(list(result))
