import subprocess

def run(cmd):
    subprocess.run(cmd, shell=True)

# Push changes to GitHub
run("git push origin main")

print("Code pushed to GitHub successfully")
