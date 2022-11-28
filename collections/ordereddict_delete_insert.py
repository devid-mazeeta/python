# A Python program to demonstrate working
# of OrderedDict

from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

print('Before Deleting')
for key, value in od.items():
	print(key, value)

# deleting element
od.pop('a')

# Re-inserting the same
od['a'] = 9

print('\nAfter re-inserting')
for key, value in od.items():
	print(key, value)
