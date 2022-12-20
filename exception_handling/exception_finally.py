try:
   fh = open("sample.txt", "w")
   fh.read("hello python")
except TypeError:
   print ("'Sample.txt' doesn't exits")
finally: # this block is executed compulsarily eventhogh the exception is occured or not in try block
   print ("File written successfully")
   fh.close()
