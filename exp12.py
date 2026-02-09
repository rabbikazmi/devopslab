import os
import time

file_name = "sample.txt"
log_file = "file_changes.log"

if os.path.exists(file_name):
    modified_time = os.path.getmtime(file_name)
    readable_time = time.ctime(modified_time)

    with open(log_file, "a") as log:
        log.write(f"{file_name} modified at {readable_time}\n")

    print("File change logged")
else:
    print("File not found")
