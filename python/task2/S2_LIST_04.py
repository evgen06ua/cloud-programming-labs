def flatten1(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            for x in item:
                result.append(x)
        else:
            result.append(item)
    return result

lst = [1, [2, 3], 4, [5, 6, 7], 8]
print(flatten1(lst))
