# -*- coding: utf-8 -*-
# src/graph.py
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import psutil

# Liste pour stocker l'utilisation CPU
cpu_history = []

def update_cpu(frame):
    """Fonction d'animation qui met à jour le graphique avec l'utilisation CPU."""
    cpu_usage = psutil.cpu_percent(interval=0.1)
    cpu_history.append(cpu_usage)
    # Limiter l'historique aux 50 dernières mesures
    if len(cpu_history) > 50:
        cpu_history.pop(0)
    plt.cla()  # Effacer l'axe courant
    plt.plot(cpu_history, label="CPU (%)")
    plt.ylim(0, 100)
    plt.title("Utilisation du CPU en temps réel")
    plt.xlabel("Temps (échantillons)")
    plt.ylabel("Utilisation (%)")
    plt.legend(loc="upper right")

def lancer_graphique():
    """Lance le graphique en temps réel dans une fenêtre séparée."""
    # fig = plt.figure()
    ani = animation.FuncAnimation(fig, update_cpu, interval=500)  # mise à jour toutes les 500 ms
    plt.show()

if __name__ == "__main__":
    lancer_graphique()
