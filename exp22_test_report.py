import subprocess

report = ""

def run_test(name, command):
    global report
    result = subprocess.run(command, shell=True)
    if result.returncode == 0:
        report += f"{name}: PASS\n"
    else:
        report += f"{name}: FAIL\n"

print("Running Tests...")

run_test("Test 1", "python --version")
run_test("Test 2", "python -c \"print(5+5)\"")

with open("build_report.txt", "w") as f:
    f.write(report)

print("Report Generated: build_report.txt")