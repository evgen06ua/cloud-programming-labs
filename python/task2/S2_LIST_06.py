users = [
    {"id": 1, "name": "alice", "active": True},
    {"id": 2, "name": "bob", "active": False},
    {"id": 3, "name": "charlie", "active": True},
    {"id": 4, "name": "david", "active": True}
]

active_names = [u["name"].upper() for u in users if u["active"]]
active_names = sorted(active_names)
print(active_names)
