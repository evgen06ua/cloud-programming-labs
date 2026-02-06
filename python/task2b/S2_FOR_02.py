def find_first_even(nums):
    for n in nums:
        if n % 2 == 0:
            return n
    return None

nums = [1, 3, 5, 8, 9, 10]
print(find_first_even(nums))
print(find_first_even([1, 3, 5]))
