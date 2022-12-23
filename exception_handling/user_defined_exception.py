class NetworkError(RuntimeError):
	def __init__(self, arg):
		self.msg = arg

try:
	raise NetworkError("Bad hostname") # raises an exception
except NetworkError as ne:
	print(ne.msg)
