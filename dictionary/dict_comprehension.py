fruits = {
	"apple": 10,
	"banana": 20,
	"orange": 5,
	"grapes": 6,
}

# Without Comprehension
filtered_fruits = {}
for key, value in fruits.items():
	if value >= 10:
		filtered_fruits[key] = value
print(filtered_fruits)

# Dict Comprehension
filtered_fruits = { key:value for key, value in fruits.items() if value >= 10 }
print(filtered_fruits)
