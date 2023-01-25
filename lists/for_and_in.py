# for loop [for/in]
numbers = [1,2,3,4]
print(len(numbers)) # prints length of the list
result = 0

for number in numbers:
	result += number # result = result + number
	# result = 0 + 1 # 1
	# result = 1 + 2 # 3
	# result = 3 + 3 # 6
	# result = 6 + 4 # 10

print(result)

# if statement and in
numbers1 = []
numbers2 = [1,2]

if numbers1:
	print("Values in list")
else:
	print("No values in list")

if len(numbers2) == 2:
	print("Length in list matches")

colors = ['red','white','black']

if 'white' in colors:
	print('white color is present in the list')
else:
	print('white color is not present in the list')

colors2 = ['this is red','this is white','this is black']

for color in colors2:
	print(color, end=" : ")
	if color.find('white') >= 0:
		print("yes")
	else:
		print("no")
