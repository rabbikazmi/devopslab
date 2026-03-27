import time
import random

def deploy():
    print("Deploying new version...")
    time.sleep(1)
    
    # simulate success/failure
    if random.choice([True, False]):
        print("Deployment Successful!")
        return True
    else:
        print("Deployment Failed!")
        return False

def rollback():
    print("Rolling back to previous stable version...")
    time.sleep(1)
    print("Rollback Completed!")

def pipeline():
    print("Starting Deployment Process...")
    
    success = deploy()
    
    if not success:
        rollback()
    else:
        print("No rollback needed.")

pipeline()