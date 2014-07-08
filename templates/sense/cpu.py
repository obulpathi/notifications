import psutil

def sense():
    if psutil.cpu_percent(interval=1)>{{threshold}}:
        return True, "The CPU Usage is above {{threshold}}%"

    return False, ""
