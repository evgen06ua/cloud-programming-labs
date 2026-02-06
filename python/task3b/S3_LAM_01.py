square = lambda n: n * n
is_odd = lambda n: n % 2 == 1
greet = lambda name: f"Hello, {name}!"

print(square(5))
print(square(10))
print(square(-3))

print(is_odd(7))
print(is_odd(8))
print(is_odd(0))

print(greet("Alice"))
print(greet("Bob"))
print(greet("Charlie"))
