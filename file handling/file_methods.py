import os
import time

# checks whether the file exists or not
if os.path.isfile('current_file.txt'): print ('File exists')
else: open("current_file.txt","w+")
time.sleep(10)

# renames the file
os.rename('current_file.txt','new_file.txt')
time.sleep(10)

# deletes the file
os.remove('new_file.txt')
time.sleep(10)

# creates the directory
os.mkdir("sample")
time.sleep(10)

# checks whether the directory exists or not
if os.path.isdir("sample"): print ('Directory exists')
else: print ('Directory does not exists')
time.sleep(10)

# changes the directory
os.chdir("sample")
print (os.getcwd())
time.sleep(10)

# deletes the directory
# os.rmdir(r'C:\Programming\pythontraining\file handling\sample') # Throws PermissionError
# time.sleep(10)

# returns current working directory
print (os.getcwd())
