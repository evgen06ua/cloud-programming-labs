def sum_nested(matrix):
    total = 0
    for row in matrix:
        if not isinstance(row, list):
            return None
        for num in row:
            total += num
    return total

matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(sum_nested(matrix))
print(sum_nested([[1, 2], "bad", [3]]))
