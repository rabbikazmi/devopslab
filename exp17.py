import subprocess
import os

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result

print("========== EXPERIMENT 17 ==========")

# Create new directory
repo_name = "multi_contributor_repo"

if not os.path.exists(repo_name):
    os.mkdir(repo_name)

os.chdir(repo_name)

# Initialize repository
run_command("git init")

# Create initial file
with open("file.txt", "w") as f:
    f.write("Hello World\n")

run_command("git add .")
run_command('git commit -m "Initial commit"')

# Contributor 1 branch
run_command("git checkout -b contributor1")
with open("file.txt", "w") as f:
    f.write("Change from Contributor 1\n")

run_command("git commit -am 'Contributor 1 update'")

# Switch back to main
run_command("git checkout main")

# Contributor 2 branch
run_command("git checkout -b contributor2")
with open("file.txt", "w") as f:
    f.write("Change from Contributor 2\n")

run_command("git commit -am 'Contributor 2 update'")

# Merge contributor1 into main
run_command("git checkout main")
run_command("git merge contributor1")

# Try merging contributor2 (will create conflict)
merge_result = run_command("git merge contributor2")

if merge_result.returncode != 0:
    print("\n⚠ Merge Conflict Detected!")
    print(merge_result.stderr)
else:
    print("\nMerge Successful!")

print("\nCheck file.txt manually to resolve conflict.")
