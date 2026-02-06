print("Hello from Docker! Image built and executed using Python automation.")


# Print the current date and time
from datetime import datetime
now = datetime.now()
print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

# Print the Python version
import sys
print("Python version:", sys.version)

# Print the operating system information
import platform
print("Operating System:", platform.system(), platform.release())

# Print the Docker version
import subprocess
try:
    docker_version = subprocess.check_output(["docker", "--version"]).decode().strip()
    print("Docker version:", docker_version)
except Exception as e:
    print("Error getting Docker version:", e)