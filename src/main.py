import time
import os
from system_monitor import get_system_metrics
from weather_api import get_weather
from logger import log_metrics
from display import display_metrics

REFRESH_INTERVAL = 5  # 5 secondes

def main():
    while True:
        # Nettoyage de l'écran AVANT l'affichage suivant
        os.system('cls' if os.name == 'nt' else 'clear')

        # Récupérer les métriques système
        cpu, memoire, disque, top_processus = get_system_metrics()

        # Récupérer la météo
        temperature, conditions, humidite = get_weather()

        # Afficher les données
        display_metrics(cpu, memoire, disque, top_processus, temperature, conditions, humidite)

        # Enregistrer dans le fichier log
        log_metrics(cpu, memoire, disque, top_processus, temperature)

        # Laisser l'affichage à l'écran pendant REFRESH_INTERVAL secondes
        time.sleep(REFRESH_INTERVAL)

if __name__ == "__main__":
    main()
