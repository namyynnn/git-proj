import psutil
import time

def get_system_usage():
    # CPU utilization
    cpu_percent = psutil.cpu_percent(interval=1)
    
    # Disk usage (default is main partition)
    disk_usage = psutil.disk_usage('/')
    disk_total = disk_usage.total / (1024 ** 3)  # in GB
    disk_used = disk_usage.used / (1024 ** 3)
    disk_percent = disk_usage.percent

    print(f"CPU Usage: {cpu_percent}%")
    print(f"Disk Usage: {disk_used:.2f} GB / {disk_total:.2f} GB ({disk_percent}%)")

# Loop to show usage every 5 seconds
while True:
    get_system_usage()
    print("-" * 30)
    time.sleep(5)
    ooorchillooo
