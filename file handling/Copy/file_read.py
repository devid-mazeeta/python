# accessing/reading the file
file = open('sample1.txt', 'r')
# file = open('C:\Users\gdevid\Downloads\AH\input_contract.json', 'r')
print(file)
for line in file:
	print (line, end="")
	print (file.read(5))
	# file.seek(0,0)
file.close()
