print(range(100), end="\n\n")
print(list(range(100)), end="\n\n")

# range with single argument
for n in range(100):
	print(n, end=' ') # prints 0 to 99
print("\n")

# range with double arguments
for n in range(20,30):
	print(n, end=' ') # prints 20 to 29
print("\n")

# range with triple arguments
for n in range(20,30,2):
	print(n, end=' ') # prints 20,22,24,26,28
print("\n")

# range with triple arguments in reverse
for n in list(range(20,30,2))[::-1]:
	print(n, end=' ') # prints 20,22,24,26,28
