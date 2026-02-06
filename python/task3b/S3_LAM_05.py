def at_least(min_value):
    return lambda n: n >= min_value

nums = [5, 10, 15, 20, 25, 30]
at_least_15 = at_least(15)
filtered = list(filter(at_least_15, nums))
print(filtered)
