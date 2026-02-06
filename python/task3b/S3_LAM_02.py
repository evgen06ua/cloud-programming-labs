people = [
    {"name": "alice", "age": 30},
    {"name": "bob", "age": 25},
    {"name": "charlie", "age": 35}
]

print("Before:")
print(people)

sorted_people = sorted(people, key=lambda p: p["age"])

print("After:")
print(sorted_people)
