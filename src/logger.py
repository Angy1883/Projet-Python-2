# src/logger.py
import os
from datetime import datetime

LOG_DIR = "logs"

def log_metrics(cpu, memoire, disque, top_processus, temperature):
    """
    Enregistre les métriques principales dans un fichier log quotidien.
    
    Arguments:
      cpu          : Pourcentage d'utilisation du CPU.
      memoire      : Tuple (utilisé, disponible, pourcentage) de la mémoire.
      disque       : Liste de tuples (partition, utilisé, total, pourcentage) pour chaque disque.
      top_processus: Liste des top processus (pour simplifier, seuls le nom et le PID peuvent être enregistrés).
      temperature  : Température extérieure (None si indisponible).
    """
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    
    # Nom du fichier log basé sur la date du jour
    fichier_log = os.path.join(LOG_DIR, f"{datetime.now().strftime('%Y-%m-%d')}.log")
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    ligne_log = (
        f"{timestamp} | CPU: {cpu}% | Mémoire: {memoire[2]}% "
        f"(Utilisé: {memoire[0]:.2f}GB, Disponible: {memoire[1]:.2f}GB) | "
        f"Disque: {[ (d[0], f'{d[3]}%') for d in disque ]} | "
        f"Météo: {temperature if temperature is not None else 'N/A'}°C\n"
    )
    
    with open(fichier_log, 'a', encoding='utf-8') as f:
        f.write(ligne_log)

if __name__ == "__main__":
    # Exemple de test
    cpu = 78.5
    memoire = (10.9, 16.0, 68.2)
    disque = [("C:\\", 189.2, 298.5, 63.4), ("D:\\", 154.0, 500.0, 30.8)]
    top_processus = []
    temperature = 24.5
    log_metrics(cpu, memoire, disque, top_processus, temperature)
    print("Log écrit.")
