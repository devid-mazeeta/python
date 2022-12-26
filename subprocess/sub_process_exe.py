import os
import sys
import subprocess

dir_path = r'C:\Programming\pythontraining\subprocess'
os.chdir(dir_path) # changes the working directory
script_path = os.path.join(dir_path, 'sub_script.py') # joins the script path
command = r'python "'+script_path+'"' # command to execute
print(command)

(status1, terminallog) = subprocess.getstatusoutput(command) # returns both the status and output
status2 = os.system(command) # returns only the status

# Status
# 0 => no error
# 1 => contains error

if status1:
	print(status1)
	print(status2)
	print(terminallog)
	sys.stderr.write(terminallog)
	sys.exit()
else:
	print(status1)
	print(status2)
	print(terminallog)

print("\nTest Sys")
