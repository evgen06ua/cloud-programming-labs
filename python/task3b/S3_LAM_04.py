from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda n: n % 2 == 0, nums))
print("Evens:", evens)

squares = list(map(lambda n: n * n, evens))
print("Squares:", squares)

total = reduce(lambda a, b: a + b, squares)
print("Sum:", total)
