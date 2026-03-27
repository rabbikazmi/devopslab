import psutil
import time

def check_health():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print(f"\nCPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")

    if cpu > 80:
        print("⚠️ High CPU usage!")
    if memory > 80:
        print("⚠️ High Memory usage!")
    if disk > 80:
        print("⚠️ Low Disk Space!")

while True:
    check_health()
    time.sleep(5)   # check every 5 seconds