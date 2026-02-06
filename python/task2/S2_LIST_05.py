def stats(nums):
    if len(nums) == 0:
        return None
    total = sum(nums)
    avg = total / len(nums)
    return {
        "min": min(nums),
        "max": max(nums),
        "avg": avg,
        "sum": total
    }

nums = [10, -5, 3, 7, -2]
print(stats(nums))
print(stats([]))
