def sum_until(nums, threshold):
    total = 0
    for n in nums:
        if total + n > threshold:
            break
        total += n
    return total

nums = [5, 10, 15, 20, 25]
print(sum_until(nums, 30))
print(sum_until(nums, 50))
