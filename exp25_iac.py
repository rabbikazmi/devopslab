import os

print("Simulating Infrastructure Setup...")

folders = ["server", "database", "network"]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created: {folder}")

print("Infrastructure setup completed ")