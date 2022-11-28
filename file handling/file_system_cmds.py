import os
import shutil

def printdir(dir):
	filenames = os.listdir(dir)
	print ('List of filename:'+str(filenames))
	for filename in filenames:
		print (filename)
		fullpath=os.path.join(dir, filename)
		print (fullpath)
		absolute = os.path.abspath(fullpath)
		print (absolute)
		dirname = os.path.dirname(absolute)
		print (dirname)
		file = os.path.basename(absolute)
		print (file)
		result=os.path.exists(dir)
		print (result)

		if filename != 'Copy':
			if not os.path.isdir('Copy'):
				os.mkdir("Copy")

			shutil.copy(absolute, 'Copy')

if __name__ == '__main__':
	dir = r'../file handling'
	printdir(dir)
