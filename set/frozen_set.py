mylist = ['a', 'b', 'c', 'a']
# mytuple = ('a', 'b', 'c', 'a')
# mydict = {'a':1, 'b':2, 'c':5, 'a':10}
myset = {'a', 'b', 'c', 'a'}
print(myset)

### Syntax ###
# frozenset(iteratable)

### Convert to frozen set ###
myfrozenset = frozenset(mylist)
print(myfrozenset)

# Exception -> TypeError: 'frozenset' object does not support item assignment
# myfrozenset[1] = "d" # frozenset cant be modified
