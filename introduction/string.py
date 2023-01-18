# printing integer
number = 10
print(number)

# int+int => sum
print(10 + 10) # 20
# str+str => concatenation
print('10' + '10') # 1010
# str+int (or) int+str => TypeError
# print('10' + 10) # TypeError: can only concatenate str (not "int") to str

# adding integer to the integer
output = number + 20
print(output)

# printing string
name_1 = 'python'
print(name_1)

# finding length of the string
name_2 = 'language'
print(len(name_2))
print(type(name_2))
print(type(len(name_2)))

# concatenation of strings
output = name_1 + name_2
print(output)

# adding integer to the string | integer converted to string type
# output = name_1 + ' ' + len(name_2) # Raise TypeError
output = name_1 + ' ' + str(len(name_2))
print(output)

# adding integer to the string | string converted to integer type
num = '8'
print(8 + int(num))
# num = 'abc'
# print(8 + int(num)) # ValueError: invalid literal for int() with base 10: 'abc'
