def unique(values):
    result = []
    for v in values:
        if v not in result:
            result.append(v)
    return result

values = [1, 2, 2, 3, 1, 4, 3, 5]
print(unique(values))
