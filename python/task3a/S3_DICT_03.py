def pick(d, keys):
    result = {}
    for k in keys:
        if k in d:
            result[k] = d[k]
    return result

d = {"a": 1, "b": 2, "c": 3, "d": 4}
print(pick(d, ["a", "c", "x"]))
