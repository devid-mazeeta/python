num1 = 100
num2 = 100
num3 = 200

# method 1
if num1 == num2:
	print("'num1' equal to 'num2'")

	if num1 > num3:
		print("'num1' greater than 'num3")
	elif num3 > num2:
		print("'num3' greater than 'num2'")
	else:
		print("prints when no statement matches")
else:
	print("'num1' not equal to 'num2'")

# method 2
if num1 == num2:
	print("'num1' equal to 'num2'")
	if num1 > num3: print("'num1' greater than 'num3")
	elif num3 > num2: print("'num3' greater than 'num2'")
	else: print("prints when no statement matches")
else: print("'num1' not equal to 'num2'")

### if not ###

if not(num1 == num2): # if num1 != num2:
	print("'num1' equal to 'num2'")
else:
	print("'num1' not equal to 'num2'")

###

text1 = 'abc'

if text1:
	print('exists')

###

text2 = None

if not text2:
	print('exists')

### is ###

number1 = 10
number2 = 10

if number1 is number2:
	print("Equal")
