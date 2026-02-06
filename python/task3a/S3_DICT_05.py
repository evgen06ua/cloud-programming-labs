def invert(d):
    result = {}
    for k, v in d.items():
        if v in result:
            if not isinstance(result[v], list):
                result[v] = [result[v]]
            result[v].append(k)
        else:
            result[v] = k
    return result

d = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
print(invert(d))
