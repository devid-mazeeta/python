# Python program to illustrate the concept of threading
# importing the threading module
import threading

def print_square(num):
	# function to print square of given num
	print("Square: {}" .format(num * num))

def print_cube(num):
	# function to print cube of given num
	print("Cube: {}" .format(num * num * num))

def print_number(num):
	for x in range(num):
		print(x)

def print_text(num):
	for x in range(num):
		print('a')

if __name__ =="__main__":
	# creating thread
	t1 = threading.Thread(target=print_square, args=(10,))
	t2 = threading.Thread(target=print_cube, args=(10,))
	t3 = threading.Thread(target=print_number, args=(100,))
	t4 = threading.Thread(target=print_text, args=(100,))

	# starting thread 1
	t1.start()
	# starting thread 2
	t2.start()
	# starting thread 3
	t3.start()
	# starting thread 4
	t4.start()

	# wait until thread 1 is completely executed
	t1.join()
	# wait until thread 2 is completely executed
	t2.join()
	# wait until thread 3 is completely executed
	t3.join()
	# wait until thread 4 is completely executed
	t4.join()

	# all threads completely executed
	print("Done!")
