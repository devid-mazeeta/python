# accessing/reading the file
# file = open('C:/Users/gdevid/Downloads/AH/sample1.txt', 'r')
file = open('sample1.txt', 'r')
print(file)
print(type(file))
count = 1

for line in file:
	print (line, end="")
	print (file.read(5))

	# if count <= 5:
	# 	file.seek(0,0)
	# 	count += 1
file.close()
