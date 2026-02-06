lines = [
    "INFO: user=42 action=login",
    "ERROR: user=99 action=fail",
    "INFO: user=15 action=logout",
    "INFO: user=42 action=view"
]

user_ids = []
for line in lines:
    if not line.startswith("INFO:"):
        continue
    parts = line.split()
    for part in parts:
        if part.startswith("user="):
            user_str = part.split("=")[1]
            try:
                user_id = int(user_str)
                user_ids.append(user_id)
            except:
                pass

print(user_ids)
