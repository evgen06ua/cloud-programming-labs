def merge_defaults(defaults, overrides):
    return {**defaults, **overrides}

defaults = {"host": "localhost", "port": 8080, "debug": False}
overrides = {"port": 3000, "debug": True}
merged = merge_defaults(defaults, overrides)
print(merged)

defaults2 = {"a": {"nested": 1}}
overrides2 = {"a": {"other": 2}}
merged2 = merge_defaults(defaults2, overrides2)
print(merged2)
