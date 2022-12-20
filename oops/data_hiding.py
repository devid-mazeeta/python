class TokenCounter:
   __hiddenCount = 0 # data hiding
  
   def counter(self):
      self.__hiddenCount += 1
      print(self.__hiddenCount)

number = TokenCounter()
number.counter()
number.counter()
print (number.__hiddenCount)
