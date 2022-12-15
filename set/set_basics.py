# Set -> It will not hold any duplicate elements
numbers = {10,20,20,30}
print(type(numbers))
print(numbers)

numbers1 = {10,20,20,30} # 3 unique elements
numbers2 = {10,20,20,30,40} # 4 unique elements

if numbers1 > numbers2:
	print("numbers1")
else:
	print("numbers2")
