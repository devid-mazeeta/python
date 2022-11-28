# for loop [for/in]
numbers = [1,2,3,4]
print(len(numbers)) # prints length of the list
result = 0

for num in numbers:
	result += num
	# result = result + num

print (result)

# if statement [in]

numbers1 = []
numbers2 = [1,2]

if numbers1:
	print("Values in list")
else:
	print("No values in list")

if len(numbers2) == 2:
	print("Values in list")

colors = ['red','white','black']

if 'white' in colors:
	print ('white color is present in the list')
else:
	print ('white color is not present in the list')
