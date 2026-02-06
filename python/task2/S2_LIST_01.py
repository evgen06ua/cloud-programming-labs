def clean_numbers(values):
    result = []
    for v in values:
        v = v.strip()
        try:
            num = float(v)
            result.append(num)
        except:
            pass
    return result

values = [" 1 ", "x", "2", " 3.5 ", "abc", "10"]
cleaned = clean_numbers(values)
print(cleaned)
