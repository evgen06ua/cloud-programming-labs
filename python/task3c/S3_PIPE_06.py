def pipe_safe(*fns):
    def apply(x):
        result = x
        try:
            for fn in fns:
                result = fn(result)
            return {"ok": True, "value": result}
        except Exception as e:
            return {"ok": False, "error": str(e)}
    return apply

add5 = lambda x: x + 5
divide_by_zero = lambda x: x / 0

safe_fn = pipe_safe(add5, divide_by_zero)
result = safe_fn(10)
print(result)

safe_fn2 = pipe_safe(add5, lambda x: x * 2)
result2 = safe_fn2(10)
print(result2)
