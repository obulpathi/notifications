import psutil

def sense():
    mem = psutil.virtual_memory()
    if mem.percent > {{threshold}}:
        return True, "The memory usage is above {{threshold}}%"

