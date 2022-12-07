# sorted vs sort()
numbers = [2,1,3]
print(sorted(numbers)) # Sorts in temp memory
print(numbers)
print(numbers[1])
print(numbers.sort()) # Affects orginal memory
print(numbers)
print(numbers[1])

# sorted(reverse=True) vs reverse()
numbers2 = [1,24,57,84,12,23]
print(sorted(numbers2, reverse=True))
print(numbers2[1])
print(numbers2.sort())
print(numbers2.reverse())
print(numbers2)

# string sorting
numbers3 = ['1', '20', '10', '11', '100', '30', '50', '200']
numbers3.sort()
print(numbers3)
