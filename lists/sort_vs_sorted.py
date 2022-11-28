# sorted vs sort()
numbers = [2,1,3]
print(sorted(numbers))
print(numbers[1])
print(numbers.sort())
print(numbers[1])

# sorted(reverse=True) vs reverse()
numbers = [1,24,57,84,12,23]
print(sorted(numbers, reverse=True))
print(numbers[1])
print(numbers.sort())
print(numbers.reverse())
print(numbers)
