import re

text1 = '<title1>Regular Expression</title1>'
regex1 = r'<[a-z0-9]+>'
# regex1 = r'<[^>]*?>[^>]*?<\/\1>'
com1 = re.compile(regex1)
print(com1) # re.compile('<([^>]*?)>[^>]*?<\\/\\1>')
mat1 = com1.match(text1)
print(mat1)
print(mat1.group())
print(mat1.span())
print(mat1.start())
print(mat1.end())

##################################################

text2 = '<title1>Regular Expression</title1><title2>Python Language</title2>'
regex2 = '<(?P<one>[^>]*?)>[^>]*?<\/(?P=one)>'
com2 = re.compile(regex2)
print(com2) # re.compile('<(?P<one>[^>]*?)>[^>]*?<\\/(?P=one)>')
mat2 = com2.finditer(text2)
print(mat2)

for word in mat2:
	print(word) # match object
	print(word.group()) # returns whole match
	print(word.span()) # provides start and end index of the match
	print(word.start()) # provides start index of the match
	print(word.end()) # provides end index of the match

##################################################
