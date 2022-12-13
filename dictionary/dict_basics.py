# method 1
dict_1 = {} # declaring an empty dictionary\
dict_1['arun'] = 22 # adding elements to the dictionary
dict_1['joel'] = 23
dict_1['alex'] = 25
print(dict_1)

# method 2
dict_2 = {'arun':22, 'joel':23, 'alex':25}  # declaring & defining the dictionary
print(dict_2)

###################################################

dict_2['arun'] = 24 # puts new key/value to the dictionary. now it alters the value of the key 'arun'
print(dict_2)
print(dict_2['alex']) # lookup the value of the key 'alex'
# print(dict_2['hary']) # KeyError
print(dict_2.get('hary')) # omits KeyError

# None working
if dict_2.get('hary'):
	print("yes")
else:
	print("no")

###################################################

print('joel' in dict_2) # checks whether the key is present in the dictionary

if 'hary' in dict_2: print(dict_2['hary'])
else: print("key doesn't exists")

###################################################

# iterating the dictionary using keys (method 1)
for key in dict_2: print(key)

# iterating the dictionary using keys (method 2)
for key in dict_2.keys(): print(key)
print(dict_2.keys())

# iterating the dictionary using values
for value in dict_2.values(): print(value)
print(dict_2.values())

# iterating the dictionary using both the keys & values
for key, value in dict_2.items(): print(key + ' ==> '+ str(value))
print(dict_2.items())

# iterating the dictionary using keys in sorted order
for key in sorted(dict_2.values()): print(key)
