import subprocess

def run_git_command(command):
    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )
    return result.stdout

print("Generating Versioning Report...")

# Commit history
log_output = run_git_command(["git", "log", "--pretty=format:%h - %an - %ar - %s"])

# Author-wise report
author_output = run_git_command(["git", "shortlog", "-sn"])

# Save to file
with open("version_report.txt", "w") as f:
    f.write("==== Commit History ====\n")
    f.write(log_output)
    f.write("\n\n==== Contributor Report ====\n")
    f.write(author_output)

print("Report generated successfully as version_report.txt")