name = 'python' # index [0 to 5] in forward or [-1 to -6] in reverse

##### zero-based index numbers #####

# 'yth' -> character starts from index 1 and extends up to index 3. Doesn't include index 4
print(name[1:4])

# 'ython' -> character starts from index 1 and extends up to the end
print(name[1:])

# 'python' -> returns entire string
print(name[:]) # similar -> print(name)

# 'ython' -> character starts from index 1 and extends up to index 100
# Since 100 is a bigger index than string length, other indexes are truncated
print(name[1:100])

##### negative index numbers #####

# 'n' -> last character (or) 1st character from the end
print(name[-1])

# 't' -> 4th character from the end
print(name[-4])

# 'pyt' -> form 1st character to 4th character from the end. Doesn't include 3rd from the end.
print(name[:-3])

# 'hon' -> starts from 3rd character from the end and extends to the end of the string.
print(name[-3:])
