strings1 = ['DDD','aaaa','cc','B','eE']

print(sorted(strings1)) # sorts the list in the order -> (uppercase, lowercase, combined case)
print(sorted(strings1,key=len)) # sorts the list based on the elements length
print(sorted(strings1,key=str.lower)) # sorts the list without considering its case and element length

# sorts the list based on the function defined.
# ie., sorts the list in ascending order based on the last letter of the string
def myfn(value):
	return value[-1] # returns the last letter of the string

strings2 = ['xc','wd','za','yb']
print(sorted(strings2, key=myfn))
