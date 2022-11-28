try:
   fh = open("sample.txt", "r")
   fh.write("hello python")
except IOError:
   print ("'Sample.txt' doesn't exits")
   # raise Exception() # raises the exception and doesn't executes the codes hereafter
   # print ("'Sample.txt' doesn't exits")
else: # executes when no exception occurs
   print ("File written successfully")
   fh.close()
