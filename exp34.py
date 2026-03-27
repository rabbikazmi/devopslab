log_file = "log.txt"

error_count = 0
warning_count = 0

with open(log_file, "r") as file:
    lines = file.readlines()

for line in lines:
    if "ERROR" in line:
        print("ERROR:", line.strip())
        error_count += 1
    elif "WARNING" in line:
        print("WARNING:", line.strip())
        warning_count += 1

print("\nSummary:")
print("Total Errors:", error_count)
print("Total Warnings:", warning_count)