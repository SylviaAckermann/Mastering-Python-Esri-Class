

# random list of 10 numbers using random module
import random
numbers = [random.randint(1, 100) for _ in range(10)]
print(numbers)

numbers.sort()
print(numbers)

numbers_sorted = sorted(numbers)
print(numbers_sorted)