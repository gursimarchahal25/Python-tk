import time
import shutil
import psutil

def get_status(value, warn, crit):
    """Return OK, WARNING, or CRITICAL based on the value and thresholds."""
    if value >= crit:
        return "CRITICAL"
    elif value >= warn:
        return "WARNING"
    return "OK"


def check_cpu():
    value = psutil.cpu_percent(interval=1)
    return {"name": "CPU", "value": value, "status": get_status(value, 70, 90)}


def check_memory():
    value = psutil.virtual_memory().percent
    return {"name": "Memory", "value": value, "status": get_status(value, 70, 90)}


def check_disk():
    path = "/" 
    usage = shutil.disk_usage(path)
    value = round(usage.used / usage.total * 100, 1)
    return {"name": f"Disk ({path})", "value": value, "status": get_status(value, 80, 90)}


def get_uptime():
    seconds = time.time() - psutil.boot_time()
    days = int(seconds // 86400)
    hours = int((seconds % 86400) // 3600)
    minutes = int((seconds % 3600) // 60)
    return f"{days}d {hours}h {minutes}m"

    
def main():
    try:
        results = [check_cpu(), check_memory(), check_disk()]
    except Exception as error:
        print(f"Could not complete the health check: {error}")
        return


    print("=== System Health Report ===")
    for r in results:
        print(f"{r['name']:<15} {r['value']:>5}%   {r['status']}")
    print(f"{'Uptime':<15} {get_uptime()}")
    

if __name__ == "__main__":
    main()
