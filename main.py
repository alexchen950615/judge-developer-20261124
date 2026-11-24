import os

ENTRY = "It passed all my tests. Unfortunately, the users weren't in any of them."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
