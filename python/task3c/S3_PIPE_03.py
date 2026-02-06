import re

def pipe(*fns):
    def apply(x):
        result = x
        for fn in fns:
            result = fn(result)
        return result
    return apply

strip_it = lambda s: s.strip()
lowercase_it = lambda s: s.lower()
collapse_spaces = lambda s: re.sub(r'\s+', ' ', s)

normalize = pipe(strip_it, lowercase_it, collapse_spaces)

text = "  Ala  Ma   Kota  "
result = normalize(text)
print(result)
