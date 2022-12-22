import re

# string1 = "abcd123"
# string1.replace("a", "z")

text = 'a1b2c3d4e5F6G7H8I9J0'
result = re.sub('[a-z]', '', text)
print(result)
result = re.sub('[a-z]', '', text, flags=re.I)
print(result)

##################################################

text = 'one two three four five'

result = re.sub('\w+\s+', '', text)
print(result)
result = re.sub('\w+\s+', '', text, count=2) # count is used to replace the given number of matches
print(result)

##################################################

ph_no = 'tel : #950-950-9501'
result = re.sub('[\D]', '', ph_no)
print(result)

##################################################

text = 'one TWO three four five'
com = re.compile('\w+\s+', flags=re.I) # complies the regex
result = com.sub('', text, count=3)
print(result.split()) # splits the result and returns it in list

##################################################

result = re.split('[\W]+', 'one two three') # matches the regex and splits the matches in list format
print(result)

##################################################

result = re.subn('\w', 'HI' , 'one two three') # returns the replaced text and count(number of replaces)
print(result)

##################################################
