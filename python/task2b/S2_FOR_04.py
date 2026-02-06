def count_occurrences(values):
    counts = {}
    for v in values:
        if v in counts:
            counts[v] += 1
        else:
            counts[v] = 1
    return counts

values = ["a", "b", "a", "c", "b", "a", "d"]
print(count_occurrences(values))
