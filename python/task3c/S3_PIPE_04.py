def convert_numbers(values):
    for v in values:
        v = v.strip()
        try:
            yield float(v)
        except:
            pass

def double_values(values):
    for v in values:
        yield v * 2

values = [" 1 ", "x", " 2.5 ", "3", "bad", "4.0"]
converted = convert_numbers(values)
doubled = double_values(converted)
result = sum(doubled)
print(result)
