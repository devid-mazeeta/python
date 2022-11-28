# 'def' keyword is used to define the function
def add():
	num1 = 10
	num2 = 10
	num3 = num1 + num2
	return num3

def printtext():
	print("Hello World") # this statement prints only when this function is called

print("Welcome to Python")
printtext()
result = add() # result = 30
print(result)
print(add())
