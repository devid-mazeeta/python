# unicode string
u_string_1 = 'A unicode \u018e string \xf1'
print(u_string_1)

# unicode string is encoded to 'utf-8' format
utf8_string = u_string_1.encode('utf-8')
print(utf8_string)

# 'utf-8' string is decoded to unicode string
u_string_2 = str(utf8_string, 'utf-8') # unicode() in Python 2 is equivalent to str() in Python 3
print(u_string_2)

# returns 'true' if unicode string 1 equal to unicode string 2
print(u_string_1 == u_string_2)
