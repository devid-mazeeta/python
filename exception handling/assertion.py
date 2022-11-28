# assertion
def KelvinToFahrenheit(Temperature):
	assert (Temperature >= 0),"Colder than absolute zero!"
	return ((Temperature-273)*1.8)+32

print (KelvinToFahrenheit(273)) # no error - 32.0
print (int(KelvinToFahrenheit(505.78))) # no error - 451
print (KelvinToFahrenheit(-5)) # AssertionError - Colder than absolute zero!
