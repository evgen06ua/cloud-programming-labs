import math

nan1 = float("nan")

try:
    nan2 = 0.0 / 0.0
except:
    nan2 = float("nan")

print(f"nan1 == nan1: {nan1 == nan1}")
print(f"nan1 == nan2: {nan1 == nan2}")
print(f"math.isnan(nan1): {math.isnan(nan1)}")
print(f"math.isnan(nan2): {math.isnan(nan2)}")
