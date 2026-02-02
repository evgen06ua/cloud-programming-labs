big = 10 ** 100
print(f"type: {type(big).__name__}")
print(f"digits: {len(str(big))}")

big_float = float(10 ** 100)
print(f"float type: {type(big_float).__name__}")

# float loses precision with very large numbers
