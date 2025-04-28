# src/main.py
import time
import os
import threading
from rich.live import Live
from system_monitor import get_system_metrics, get_network_usage
from weather_api import get_weather
from logger import log_metrics
from display import create_display

REFRESH_INTERVAL = 5  # rafraîchissement toutes les 5 secondes

def main():
    # Utilisation de Live pour maintenir un affichage permanent
    with Live(refresh_per_second=1, screen=True) as live:
        while True:
            # Récupérer les métriques système
            cpu, memoire, disque, top_processus = get_system_metrics()
            # Récupérer les données météo
            temperature, conditions, humidite = get_weather()
            # Récupérer la surveillance réseau
            bytes_envoyes, bytes_recus = get_network_usage()

            # Créer l'affichage mis à jour
            panel = create_display(cpu, memoire, disque, top_processus,
                                   temperature, conditions, humidite,
                                   bytes_envoyes, bytes_recus)
            live.update(panel)

            # Enregistrer les métriques dans un fichier log quotidien
            log_metrics(cpu, memoire, disque, top_processus, temperature)

            # Pause pendant 5 secondes, puis réactualise
            time.sleep(REFRESH_INTERVAL)

if __name__ == "__main__":
    main()
    from rich.console import Console
    console = Console()
    
    top_processus_ex = [
        {"name": "chrome.exe", "pid": 1234, "cpu_percent": 85, "memory_info": type('mem', (object,), {"rss": 500 * 1024**2})()},
        {"name": "code.exe", "pid": 5678, "cpu_percent": 65, "memory_info": type('mem', (object,), {"rss": 800 * 1024**2})()},
        {"name": "explorer.exe", "pid": 9101, "cpu_percent": 35, "memory_info": type('mem', (object,), {"rss": 200 * 1024**2})()},
    ]

    panel = create_display(50.5, (8.2, 16.0, 51.3), [("C:\\", 120.0, 500.0, 24.0)], top_processus_ex, 22.5, "partiellement nuageux", 55, 40000000, 80000000)
    console.print(panel)
    console.print("Exécution terminée.")