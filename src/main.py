# src/main.py
import time
import os
from system_monitor import get_system_metrics
from weather_api import get_weather
from logger import log_metrics
from display import display_metrics

REFRESH_INTERVAL = 5  # Rafraîchissement toutes les 5 secondes

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        # Récupérer les métriques système
        cpu, memoire, disque, top_processus = get_system_metrics()
        # Récupérer les données météo
        temperature, conditions, humidite = get_weather()
        # Afficher les métriques et la météo dans la console
        display_metrics(cpu, memoire, disque, top_processus, temperature, conditions, humidite)
        # Enregistrer les métriques dans un fichier log quotidien
        log_metrics(cpu, memoire, disque, top_processus, temperature)
        time.sleep(REFRESH_INTERVAL)

if __name__ == "__main__":
    main()
