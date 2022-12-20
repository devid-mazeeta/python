import codecs

file = codecs.open('sample3.txt', 'r', 'utf-16')
for line in file:
	print (line) # unicode string
file.close()
