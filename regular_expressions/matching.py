import re

text1 = '#$%aaabbbccc@gmail.com#$%aaabbbccc@gmail2.net' # text to match the regular expression
# regex1 = r'([\w]+)@([\w]+\.[\w]+)' # pattern to match
regex1 = r'(\w+)@(\w+\.\w+)' # pattern to match

match1 = re.search(regex1, text1) # searches the regex pattern in the given text and returns the first match
print(match1)

# match1 = re.search(regex1, "abc") # No match
# print(match1)

if match1:
	print (match1.groups()) # returns all the group in tuple
	print (match1.group()) # returns whole match
	print (match1.group(1)) # returns first grouping
	print (match1.group(2)) # returns second grouping
	# print (match1.group(3)) # error
else:
	print ("No matches found")

#################################################

text2 = '#$%aaabbbccc@gmail.com'
regex2 = r'([\w]+)@([\w]+\.[\w]+)'

match2 = re.match(regex2, text2) # matches the regex pattern from the beginning of the given text
# match2 = re.match(regex2, text2, flags = 0) # matches the regex pattern from the beginning of the given text

if match2:
	print (match2.group())
else:
	print ("No matches found")

##################################################

text3 = 'aaabbbccc@gmail.com@#$'
regex3 = r'([\w]+)@([\w]+\.[\w]+)'

match3 = re.match(regex3, text3, re.I) # matches the regex pattern from the beginning of the given text

if match3:
	print (match3.groups())
else:
	print ("No matches found")

##################################################

text4 = """123abc456def789ghi
123JKL456MNO789PQR"""
regex4 = r'([^a-z\s]+)'
# regex4 = r'(\d+)'

match4 = re.findall(regex4, text4, re.I|re.M) # finds all the matches and returns it in list

for number in match4:
	print (number)

##################################################

text5 = "Python created by Guido Van Rossum"
regex5 = r'([\w]+)'

match5 = re.finditer(regex5, text5, re.I) # finditer() returns iteratable object
print (match5)

for word in match5:
	print (word) # Match object
	print (word.group()) # returns whole match
	print (word.span()) # provides start and end index of the match
	print (word.start()) # provides start index of the match
	print (word.end()) # provides end index of the match
	
##################################################
