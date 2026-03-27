import re

file = "code.txt"

patterns = {
    "API_KEY": r"API_KEY\s*=\s*['\"].+['\"]",
    "PASSWORD": r"PASSWORD\s*=\s*['\"].+['\"]",
    "SECRET": r"SECRET\s*=\s*['\"].+['\"]"
}

with open(file, "r") as f:
    content = f.read()

found = False

for key, pattern in patterns.items():
    matches = re.findall(pattern, content)
    if matches:
        print(f"\n{key} found:")
        for m in matches:
            print("  ", m)
        found = True

if not found:
    print("No secrets detected.")