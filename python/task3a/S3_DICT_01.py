def get_path(obj, path, fallback):
    keys = path.split(".")
    current = obj
    for key in keys:
        if not isinstance(current, dict):
            return fallback
        if key not in current:
            return fallback
        current = current[key]
    return current

obj = {"a": {"b": {"c": 42}}}
print(get_path(obj, "a.b.c", None))
print(get_path(obj, "a.b.x", "default"))
print(get_path(obj, "x.y.z", 0))
