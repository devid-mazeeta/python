# print("hello world")

# 'def' keyword is used to define the function
def add(num1, num2):
	# num1 = 10
	# num2 = 20
	newnum = num1 + num2
	return newnum

def printtext():
	"""
		This method prints few print statements
	"""

	print("Hello World 1") # this statement prints only when this function is called
	# this statement prints only when this function is called
	print("Hello World 2")

print("Welcome to Python")
printtext()
result1 = add(10,20) # 30
print(result1)
result2 = add(10,30) # 40
print(result2)
result3 = add(10,40) # 50
print(result3)
print(add(10,50)) # 60
