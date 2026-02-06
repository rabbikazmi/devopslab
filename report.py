import subprocess
import os

# Check if current directory is a Git repository
if not os.path.exists(".git"):
    print("Error: Not a Git repository")
    exit()

# Get commit history
result = subprocess.run(
    "git log --oneline",
    shell=True,
    capture_output=True,
    text=True
)

commits = result.stdout.strip().split("\n")

print("Git Commit Analysis Report")
print("--------------------------")
print("Total Number of Commits:", len(commits))
print("\nCommit History:")

for commit in commits:
    print(commit)
