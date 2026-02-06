def omit(d, keys):
    result = {}
    for k, v in d.items():
        if k not in keys:
            result[k] = v
    return result

d = {"a": 1, "b": 2, "c": 3, "d": 4}
print(omit(d, ["b", "d"]))
