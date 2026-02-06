import subprocess
import os

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

# Step 1: Check if current directory is a Git repository
if not os.path.exists(".git"):
    print("Error: This is not a Git repository.")
    exit()

print("Git repository detected")

# Step 2: Create a new branch
run("git branch dev_branch")
print("Branch 'dev_branch' created")

# Step 3: Switch to the new branch
run("git checkout dev_branch")
print("Switched to dev_branch")

# (Optional) Simulate work
with open("demo.txt", "a") as f:
    f.write("Dev branch change\n")

run("git add demo.txt")
run("git commit -m \"Added dev branch change\"")

# Step 4: Switch back to main branch
run("git checkout main")
print("Switched to main")

# Step 5: Merge the feature branch
run("git merge dev_branch")
print("dev_branch merged into main")
