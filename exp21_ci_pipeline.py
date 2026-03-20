import subprocess

def run_step(step_name, command):
    print(f"\nRunning: {step_name}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"{step_name} FAILED")
        exit()
    else:
        print(f"{step_name} SUCCESS")

print("Starting CI Pipeline...")

# Step 1: Pull latest code
run_step("Git Pull", "git pull")

# Step 2: Build (example: just checking python files)
run_step("Build", "python --version")

# Step 3: Run tests (dummy)
run_step("Test", "echo Running tests...")

print("\nCI Pipeline Completed Successfully")