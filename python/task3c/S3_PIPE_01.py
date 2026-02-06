def pipe(*fns):
    def apply(x):
        result = x
        for fn in fns:
            result = fn(result)
        return result
    return apply

add5 = lambda x: x + 5
double = lambda x: x * 2
square = lambda x: x ** 2

f = pipe(add5, double, square)
print(f(3))
