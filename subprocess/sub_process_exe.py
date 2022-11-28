import os
import sys
import subprocess

folder_path = r'C:\Programming\python\Python basics\subprocess'
os.chdir(folder_path) # changes the working directory
script_path = os.path.join(folder_path, 'sub_script.py') # joins the script path
command = r'python "'+script_path+'"' # command to execute

(status1, output) = subprocess.getstatusoutput(command) # returns both the status and output
status2 = os.system(command) # returns only the status

# Status
# 0 => no error
# 1 => has error

if status1:
	print(status1)
	print(status2)
	sys.stderr.write(output)
	sys.exit()
else:
	print(status1)
	print(status2)
	print(output)
