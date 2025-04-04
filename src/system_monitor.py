import psutil

def get_cpu_usage():
    """Retourne l'utilisation du CPU en pourcentage."""
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    """Retourne l'utilisation de la mémoire (utilisée, disponible, pourcentage)."""
    memory = psutil.virtual_memory()
    used = memory.used / (1024 ** 3)  # Convertir en GB
    available = memory.available / (1024 ** 3)
    return used, available, memory.percent

def get_disk_usage():
    """Retourne l'utilisation du disque pour chaque partition."""
    partitions = psutil.disk_partitions()
    disk_info = []
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            used = usage.used / (1024 ** 3)  # Convertir en GB
            total = usage.total / (1024 ** 3)
            percent = usage.percent
            disk_info.append((partition.device, used, total, percent))
        except PermissionError:
            continue  # Évite les erreurs si une partition est inaccessible
    return disk_info

def get_top_processes(n=3):
    """Retourne les N processus les plus gourmands en CPU."""
    processes = sorted(psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_info']),
                       key=lambda p: p.info['cpu_percent'], reverse=True)
    return processes[:n]

def get_system_metrics():
    """Récupère toutes les métriques système et les retourne sous forme de tuple."""
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()
    top_processes = get_top_processes()
    return cpu, memory, disk, top_processes

# Test rapide du module
if __name__ == "__main__":
    print("CPU Usage:", get_cpu_usage(), "%")
    print("Memory Usage:", get_memory_usage())
    print("Disk Usage:", get_disk_usage())
    print("Top Processes:", get_top_processes())
