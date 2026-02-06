import subprocess

result = subprocess.run(
    "docker build -t lab-python-image .",
    shell=True
)

if result.returncode == 0:
    print("Docker image built successfully")
else:
    print("Docker image build failed")
