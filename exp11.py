import subprocess
import os

def run(cmd):
    subprocess.run(cmd, shell=True)

# initialize Git repository
if not os.path.exists(".git"):
    run("git init")
    print("Git repository initialized")

with open("sample.txt", "w") as f:
    f.write("Initial commit file")

run("git add .")
run('git commit -m "commit for exp 11"')

print("Commit created successfully")
