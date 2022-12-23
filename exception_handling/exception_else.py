try:
   fh = open("sample.txt", "r")
   fh.write("hello python")
except IOError:
   print("'sample.txt' opened in read mode")
   raise Exception() # raises the exception and doesn't executes the codes hereafter
else: # executes when no exception occurs
   print("File written successfully")
   fh.close()
