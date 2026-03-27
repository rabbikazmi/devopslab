import sys
import psutil

def show_cpu():
    print("\n--- CPU INFO ---")
    print("CPU Usage:", psutil.cpu_percent(interval=1), "%")

def show_memory():
    mem = psutil.virtual_memory()
    print("\n--- MEMORY INFO ---")
    print("Total Memory:", mem.total)
    print("Available Memory:", mem.available)
    print("Used Memory:", mem.used)
    print("Usage:", mem.percent, "%")

def show_disk():
    disk = psutil.disk_usage('/')
    print("\n--- DISK INFO ---")
    print("Total Disk:", disk.total)
    print("Used Disk:", disk.used)
    print("Free Disk:", disk.free)
    print("Usage:", disk.percent, "%")

def show_all():
    show_cpu()
    show_memory()
    show_disk()

# CLI Handling
if len(sys.argv) < 2:
    print("\nUsage: python monitor.py [cpu | memory | disk | all]")
    sys.exit()

command = sys.argv[1].lower()

if command == "cpu":
    show_cpu()
elif command == "memory":
    show_memory()
elif command == "disk":
    show_disk()
elif command == "all":
    show_all()
else:
    print("Invalid command! Use cpu/memory/disk/all")