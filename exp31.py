# Experiment 31: End-to-End DevOps Automation Pipeline
import time
import random

def build():
    print("\n[BUILD] Compiling source code...")
    time.sleep(1)
    print("[BUILD] Build successful!")

def test():
    print("\n[TEST] Running test cases...")
    time.sleep(1)
    result = random.choice(["pass", "fail"])
    
    if result == "pass":
        print("[TEST] All tests passed!")
        return True
    else:
        print("[TEST] Tests failed!")
        return False

def deploy():
    print("\n[DEPLOY] Deploying to server...")
    time.sleep(1)
    print("[DEPLOY] Deployment successful!")

def pipeline():
    print("Starting DevOps Pipeline...")
    build()
    
    if test():
        deploy()
    else:
        print("Pipeline stopped due to test failure.")

pipeline()