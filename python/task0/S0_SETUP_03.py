def eq(actual, expected):
    if actual != expected:
        raise Exception(f"Expected {expected}, got {actual}")

eq(5, 5)
eq("hello", "hello")
print("Tests passed")
