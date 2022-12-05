# split => string to list
# join => list to string

name1 = ' oBjEcT OrIeNtEd LaNgUaGe '
name2 = '-'
name3 = ' '

# list of substrings separated by the given delimiter
print(name1.split(' ')) # list is returned using delimitting space

# joins the elements in the given list together using the string as the delimiter
texts = name1.split(' ') # ["", "oBjEcT", "OrIeNtEd", "LaNgUaGe", ""]
print(name3.join(texts)) # seperated using space

# joins the elements in the given list together using the string as the delimiter
print(name2.join(['', 'oBjEcT', 'OrIeNtEd', 'LaNgUaGe', ''])) # seperated using space
