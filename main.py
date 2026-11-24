import os

ENTRY = "It passed all my tests. Unfortunately, the users weren't in any of them."

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
