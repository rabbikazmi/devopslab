import os
import shutil

print("Starting Deployment...")

source = "app.py"
destination = "deploy/app.py"

# Create deploy folder
os.makedirs("deploy", exist_ok=True)

# Copy file (simulate deployment)
shutil.copy(source, destination)

print("Application Deployed Successfully ")