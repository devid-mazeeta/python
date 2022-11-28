class SuperMarket:
	name = 'abc'
	address = 'chennai'

	def __init__(self, customer):
		self.customer = customer

	def items(self, itemno, itemname):
		self.itemno = itemno
		self.itemname = itemname
		print(itemname)

obj = SuperMarket("Devid")
print(obj.name)
print(obj.customer)
obj.items(1, "Paste")
