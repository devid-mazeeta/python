# tuple is similar to list but it is immutable
tuple1 = (4,3,1,5,2) # with paranthesis
# tuple1 = 4,3,1,5,2, # with paranthesis
tuple2 = 'hi','hello', # without paranthesis / python understands it as tuple by seeing comma

print(tuple1)
print(len(tuple1))
print(sorted(tuple1))
print(tuple1[2])
print(tuple2[1])

name = "besant"
name = "hello"

# tuple1[2] = 6 # since tuple is immutable, we can't change the element by its index
tuple1 = (10,20,30,40,50) # but we can change the whole tuple. so, tuples are not strictly immutable
print(tuple1)

(a, b, c) = (100, 200, "python")
print (c)  ## python

a = 10
b = 20
c = 30

(a,b,c)= (10,20,30)
