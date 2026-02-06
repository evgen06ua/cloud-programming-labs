def compose(*fns):
    def apply(x):
        result = x
        for fn in reversed(fns):
            result = fn(result)
        return result
    return apply

def pipe(*fns):
    def apply(x):
        result = x
        for fn in fns:
            result = fn(result)
        return result
    return apply

add5 = lambda x: x + 5
double = lambda x: x * 2

p = pipe(add5, double)
c = compose(add5, double)

print("pipe:", p(10))
print("compose:", c(10))
