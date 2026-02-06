def chunk(lst, size):
    if size <= 0:
        return None
    result = []
    for i in range(0, len(lst), size):
        result.append(lst[i:i+size])
    return result

lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(chunk(lst, 3))
print(chunk(lst, 0))
