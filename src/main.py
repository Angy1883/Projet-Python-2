# -*- coding: utf-8 -*-
# src/main.py
import time
import os
from system_monitor import get_system_metrics, get_network_usage
from weather_api import get_weather
from logger import log_metrics
from display import display_metrics
import threading
from graph import lancer_graphique

# Dans le bloc principal, avant la boucle principale :
thread_graph = threading.Thread(target=lancer_graphique, daemon=True)
thread_graph.start()

REFRESH_INTERVAL = 5  # rafraîchissement toutes les 5 secondes

def main():
    # Dans le bloc principal, avant la boucle principale :
    thread_graph = threading.Thread(target=lancer_graphique, daemon=True)
    thread_graph.start()
    while True:
        # Effacer l'écran AVANT de réafficher les nouvelles données
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Récupérer les métriques système
        cpu, memoire, disque, top_processus = get_system_metrics()
        # Récupérer la météo
        temperature, conditions, humidite = get_weather()
        # Récupérer la surveillance réseau
        bytes_envoyes, bytes_recus = get_network_usage()
        
        # Afficher les données dans la console
        display_metrics(cpu, memoire, disque, top_processus, temperature, conditions, humidite, bytes_envoyes, bytes_recus)
        
        # Enregistrer les métriques dans un fichier log quotidien
        log_metrics(cpu, memoire, disque, top_processus, temperature)
        
        # Laisser l'affichage pendant 5 secondes exactement
        time.sleep(REFRESH_INTERVAL)

if __name__ == "__main__":
    main()
