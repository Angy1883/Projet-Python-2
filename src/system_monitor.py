# src/system_monitor.py
import psutil

def get_cpu_usage():
    """Retourne le pourcentage d'utilisation du CPU."""
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    """Retourne un tuple (utilisé, disponible, pourcentage) pour la mémoire."""
    memoire = psutil.virtual_memory()
    utilise = memoire.used / (1024 ** 3)         # Conversion en GB
    disponible = memoire.available / (1024 ** 3)
    pourcentage = memoire.percent
    return utilise, disponible, pourcentage

def get_disk_usage():
    """Retourne une liste de tuples (partition, utilisé, total, pourcentage) pour chaque disque."""
    partitions = psutil.disk_partitions()
    liste_disque = []
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            utilise = usage.used / (1024 ** 3)
            total = usage.total / (1024 ** 3)
            pourcentage = usage.percent
            liste_disque.append((partition.device, utilise, total, pourcentage))
        except PermissionError:
            continue  # Ignore les partitions inaccessibles
    return liste_disque

def get_top_processes(n=3):
    """
    Retourne une liste des n processus consommant le plus de CPU.
    On filtre pour ignorer les processus système (PID ≤ 4).
    """
    processus = list(psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'memory_info']))
    # Mettre à jour les pourcentages rapidement
    for p in processus:
        try:
            p.cpu_percent(interval=0.1)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    processus = sorted(processus, key=lambda p: p.info['cpu_percent'], reverse=True)
    processus_filtrés = [p for p in processus if p.info['pid'] > 4]
    return processus_filtrés[:n]

def get_system_metrics():
    """Retourne les métriques système sous forme de tuple (CPU, Mémoire, Disque, Top Processus)."""
    cpu = get_cpu_usage()
    memoire = get_memory_usage()
    disque = get_disk_usage()
    top_processus = get_top_processes()
    return cpu, memoire, disque, top_processus

if __name__ == "__main__":
    print("Utilisation CPU :", get_cpu_usage(), "%")
    print("Utilisation Mémoire :", get_memory_usage())
    print("Utilisation Disque :", get_disk_usage())
    print("Top Processus :", get_top_processes())
