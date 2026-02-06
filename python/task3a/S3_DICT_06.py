def group_by(items, key):
    result = {}
    for item in items:
        value = item[key]
        if value not in result:
            result[value] = []
        result[value].append(item)
    return result

items = [
    {"name": "alice", "age": 25},
    {"name": "bob", "age": 30},
    {"name": "charlie", "age": 25},
    {"name": "david", "age": 30}
]
print(group_by(items, "age"))
