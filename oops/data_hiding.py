class TokenCounter:
	hiddencount = 0 # data hiding

	def counter(self):
		self.hiddencount += 1
		print(self.hiddencount)

number = TokenCounter()
number.counter()
number.counter()
print(number.hiddencount)
