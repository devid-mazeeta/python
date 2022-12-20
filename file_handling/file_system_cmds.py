import os
import shutil

def printdir(dirpath):
	filenames = os.listdir(dirpath)
	print('List of filename:'+str(filenames))
	for filename in filenames:
		print(filename)
		fullpath=os.path.join(dirpath, filename)
		print(fullpath)
		absolute = os.path.abspath(fullpath)
		print(absolute)
		dirname = os.path.dirname(absolute)
		print(dirname)
		file1 = os.path.basename(absolute)
		print(file1)
		result=os.path.exists(dirpath)
		print(result)

		if filename != 'Copy':
			if not os.path.isdir('Copy'):
				os.mkdir("Copy")

			shutil.copy(absolute, 'Copy')

if __name__ == '__main__':
	directory = r'../file_handling'
	printdir(directory)
