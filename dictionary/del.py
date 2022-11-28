count = 100
print (count)
del count # count variable is deleted
# print (count) # NameError: name 'count' is not defined

samlist = ['a','b','c','d','e','f']
print (samlist)
print (len(samlist))
del samlist[0]
print (samlist)
print (len(samlist))
del samlist[-2:]
print (samlist)
print (len(samlist))

dict = {'a':1, 'b':2, 'c':3, 'd':4}
print (dict)
print (len(dict))
del dict['b']
print (dict)
print (len(dict))
