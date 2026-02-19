import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

print("----- GIT AUTOMATION STARTED -----")

# Pull latest changes
print("\nPulling latest changes...")
pull_output = run_command("git pull")
print(pull_output)

# Check status
print("\nChecking repository status...")
status_output = run_command("git status")
print(status_output)

# Verify latest commit
print("\nLatest commit details:")
log_output = run_command("git log -1")
print(log_output)

print("\n----- GIT AUTOMATION COMPLETED -----")
