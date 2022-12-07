# Defining list with values
names1 = ["Gokul", "Jay"]

# Declaring empty list and defining later
names2 = []
names2.append("Gokul") # ["Gokul"]
names2.append("Jay") # ["Gokul", "Jay"]
print(names2)

names3 = ["Gokul", "Jay"]
names3.insert(1, "Ajay") # ["Gokul", "Ajay", "Jay"]
names3.insert(2, "Alex") # ["Gokul", "Ajay", "Alex", "Jay"]
print(names3)

# list build up
names4 = [] # create a empty list
names4.append('java')  # add an element to the list
names4.append('python')
names4.append('sql')
names4.append('perl')

print(names4) # ['java', 'python', 'sql', 'perl']
print(len(names4)) # 4
