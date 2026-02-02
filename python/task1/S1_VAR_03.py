lst = [1, 2, 3]
lst[0] = 10
print(f"list after change: {lst}")

tup = (1, 2, 3)
try:
    tup[0] = 10
except Exception as e:
    print(f"tuple error: {e}")

# lists can be changed, tuples cannot
