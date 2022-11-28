num1 = 100
num2 = 100
num3 = 200

# method 1
if num1 == num2:
	print ("'num1' equal to 'num2'")

	if num1 > num3:
		print ("'num1' greater than 'num3")
	elif num3 > num2:
		print ("'num3' greater than 'num2'")
	else:
		print ("prints when no statement matches")
else:
	print ("'num1' not equal to 'num2'")

# method 2
if num1 == num2:
	print ("'num1' equal to 'num2'")
	if num1 > num3: print ("'num1' greater than 'num3")
	elif num3 > num2: print ("'num3' greater than 'num2'")
	else: print ("prints when no statement matches")
else: print ("'num1' not equal to 'num2'")
