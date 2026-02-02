def normalize_name(x):
    if not x:
        return "Anonymous"
    
    result = x.strip()
    if not result:
        return "Anonymous"
    
    return result

print(normalize_name(""))
print(normalize_name(" "))
print(normalize_name(None))
print(normalize_name(" Ola "))
