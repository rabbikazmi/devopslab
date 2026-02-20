import os

# Required folders and files
required_items = [
    "multi_contributor_repo",
    "README.md",
    "Dockerfile",
    "exp19.py",
    "exp20.py"
]

print("Validating DevOps Lab Structure...\n")

missing = []

for item in required_items:
    if os.path.exists(item):
        print(f"[OK] {item} exists")
    else:
        print(f"[MISSING] {item}")
        missing.append(item)

if not missing:
    print("\nProject structure is VALID")
else:
    print("\nProject structure is INCOMPLETE")