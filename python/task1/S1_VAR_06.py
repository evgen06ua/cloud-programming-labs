def to_int_or_none(s):
    if s is None:
        return None
    try:
        return int(s)
    except:
        return None

print(to_int_or_none("12"))
print(to_int_or_none(" 12 "))
print(to_int_or_none("12x"))
print(to_int_or_none(""))
print(to_int_or_none(None))
