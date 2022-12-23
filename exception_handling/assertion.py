# assertion
def fahrenheittocelsius(temperature):
	assert (temperature >= 0), "Colder than absolute zero!"
	return ((temperature-273)*1.8) + 32

print(fahrenheittocelsius(279)) # no error - 42.8
print(int(fahrenheittocelsius(505.78))) # no error - 451
print(fahrenheittocelsius(-5)) # AssertionError - Colder than absolute zero!
