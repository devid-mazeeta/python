name1 = ' oBjEcT OrIeNtEd LaNgUaGe '
name2 = 'a'
name3 = ' '
name4 = '1234'

# returns the lowercase version of the string
print(name1.lower())

# returns the uppercase version of the string
print(name1.upper())

# returns a string with whitespace removed from the start and end of the string
print(name1.strip())

# centers the string using given length
print(name1.center(50))

# tests if all the string chars are in the various character classes
print(name1.isalpha())
print(name2.isalpha())
print(name1.isspace())
print(name3.isspace())
print(name1.isdigit())
print(name4.isdigit())

# tests if the string starts or ends with the given other string
print(name1.startswith('oBjEcT'))
print(name1.startswith(' oBjEcT'))
print(name1.endswith('LaNgUaGe'))
print(name1.endswith('LaNgUaGe '))

# searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found
print(name1.find('OrIeNtEd')) # 8
print(name1.find('OrIeNtED')) # -1

# returns a string where all occurrences of 'oBjEcT' have been replaced by 'Structure'
print(name1.replace('oBjEcT', 'Structure'))

# list of substrings separated by the given delimiter
print(name1.split(' ')) # list is returned using delimitting space

# List Method - join()
# joins the elements in the given list together using the string as the delimiter
print(name3.join(['', 'oBjEcT', 'OrIeNtEd', 'LaNgUaGe', ''])) # seperated using space
