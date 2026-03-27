import os
import time
import logging

# Setup logging
logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Step 1: SCM (Simulate pulling code)
def pull_code():
    print("Pulling code from repository...")
    time.sleep(1)
    
    os.makedirs("repo", exist_ok=True)
    with open("repo/app.py", "w") as f:
        f.write("print('Hello from App')\n")
    
    logging.info("Code pulled from SCM")
    return True

# Step 2: Build
def build():
    print("Building application...")
    time.sleep(1)
    
    if os.path.exists("repo/app.py"):
        logging.info("Build successful")
        return True
    else:
        logging.error("Build failed")
        return False

# Step 3: Test
def test():
    print("Running tests...")
    time.sleep(1)
    
    try:
        with open("repo/app.py", "r") as f:
            content = f.read()
        
        if "print" in content:
            logging.info("Tests passed")
            return True
        else:
            logging.warning("Tests failed")
            return False
    except:
        logging.error("Test error")
        return False

# Step 4: Docker Build (Simulation)
def docker_build():
    print("Building Docker image...")
    time.sleep(1)
    
    os.makedirs("docker", exist_ok=True)
    with open("docker/image.txt", "w") as f:
        f.write("Docker Image for app\n")
    
    logging.info("Docker image created")
    return True

# Step 5: Docker Run (Simulation)
def docker_run():
    print("Running Docker container...")
    time.sleep(1)
    
    with open("docker/container.txt", "w") as f:
        f.write("Container is running\n")
    
    logging.info("Container started")
    return True

# Final Pipeline
def pipeline():
    print("Starting DevOps Pipeline...\n")
    logging.info("Pipeline started")

    if not pull_code():
        print("SCM failed")
        return
    
    if not build():
        print("Build failed")
        return
    
    if not test():
        print("Tests failed")
        return
    
    if not docker_build():
        print("Docker build failed")
        return
    
    if not docker_run():
        print("Deployment failed")
        return

    print("\nPipeline executed successfully!")
    logging.info("Pipeline completed successfully")

# Run
if __name__ == "__main__":
    pipeline()