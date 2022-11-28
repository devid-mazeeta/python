# both the reading and writing of file
with open('xxx.png','rb') as file1, open('yyy.png','wb') as file2:
	while True:
		byte = file1.read(1)
		if byte:
			file2.write(byte)
		else: break
