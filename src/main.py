# -*- coding: utf-8 -*-
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
