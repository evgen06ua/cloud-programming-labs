def map_values(d, fn):
    return {k: fn(v) for k, v in d.items()}

d = {"a": 1, "b": 2, "c": 3}
doubled = map_values(d, lambda x: x * 2)
print(doubled)

squared = map_values(d, lambda x: x ** 2)
print(squared)
