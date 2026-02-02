def inspect(v):
    is_iterable = False
    try:
        iter(v)
        is_iterable = True
    except:
        pass
    
    return {
        "type_name": type(v).__name__,
        "is_none": v is None,
        "is_callable": callable(v),
        "is_iterable": is_iterable,
        "truthy": bool(v)
    }

values = [42, "hello", [], None, {}, lambda x: x, 0, [1,2], True, 3.14]

for v in values:
    print(f"{repr(v)} -> {inspect(v)}")
