try:
   fh = open("sample.txt", "w")
   fh.read("hello python")
except TypeError:
   print("'sample.txt' is opened in write mode")
finally: # this block is executed compulsarily eventhogh the exception is occured or not in try block
   print("File closed successfully")
   fh.close()
