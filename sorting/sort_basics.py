numbers1 = [8,6,5,50,10,1]
numbers2 = ['8','6','5','50','10','1']
alphabets = ['h','f','d','a','r','v']
strings = ['DD','aa','cc','BB','Ea']

print(sorted(numbers1))
print(sorted(numbers2))
print(sorted(alphabets))
print(sorted(strings))

print(numbers1)  # sorted() - doesn't sorts the list permanently. No changes will happen to the list
numbers1.sort()
print(numbers1) # sort() - sorts the list permanently

print(sorted(alphabets, reverse=True)) # sorts the list in reverse order
