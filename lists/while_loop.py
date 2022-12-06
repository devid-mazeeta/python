# while loop

# Example 1 -> Print 1 to 10
num = 1

while num < 11:
	print(num)
	num += 1

# Example 2 -> 
number = 1

while number > 0:
	number += 1 # number = number + 1

	if number == 5:
		continue # jumps to the next iteration

	if number == 10:
		break # ends the iteration of while loop

	print(number) # 2 3 4 6 7 8 9

print("loop ends after break")
