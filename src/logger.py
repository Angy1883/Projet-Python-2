import os
from datetime import datetime

# Dossier où seront enregistrés les logs
LOG_DIR = "logs"

def log_metrics(cpu, memory, disk, top_processes, temperature):
    """
    Enregistre les métriques dans un fichier log quotidien.
    
    Arguments:
      cpu         : Utilisation du CPU (en %)
      memory      : Tuple (used, available, percent) de la mémoire
      disk        : Liste de tuples contenant les informations de chaque partition (device, used, total, percent)
      top_processes: Liste des top processus (peut être simplifié pour l'enregistrement)
      temperature : Température extérieure récupérée (peut être None si indisponible)
    """
    # Créer le dossier LOG_DIR s'il n'existe pas
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    
    # Nom du fichier log basé sur la date du jour
    log_file = os.path.join(LOG_DIR, f"{datetime.now().strftime('%Y-%m-%d')}.log")
    
    # Format de la ligne de log avec un horodatage
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Format d'enregistrement des données
    # Pour simplifier, on enregistre quelques métriques clés
    log_line = (
        f"{timestamp} | CPU: {cpu}% | Memory: {memory[2]}% "
        f"(Used: {memory[0]:.2f}GB, Available: {memory[1]:.2f}GB) | "
        f"Disk: {[(d[0], f'{d[3]}%') for d in disk]} | "
        f"Weather: {temperature if temperature is not None else 'N/A'}°C\n"
    )
    
    # Écriture dans le fichier log (en mode ajout)
    with open(log_file, 'a') as f:
        f.write(log_line)

# Test rapide du module
if __name__ == "__main__":
    # Exemple de métriques pour tester le log
    cpu = 21.5
    memory = (5.54, 1.40, 79.9)
    disk = [('C:\\', 46.77, 80.0, 58.5), ('D:\\', 0.94, 381.33, 0.2)]
    top_processes = []  # Pour ce test, on peut ignorer cette donnée ou y mettre un exemple
    temperature = 23.5
    
    log_metrics(cpu, memory, disk, top_processes, temperature)
    print("Les métriques ont été enregistrées dans le fichier log.")
