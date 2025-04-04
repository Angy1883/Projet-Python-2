# -*- coding: utf-8 -*-
# src/display.py
from datetime import datetime
from rich.console import Group, Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

console = Console()

def get_cpu_color(cpu_percent):
    """Retourne la couleur selon le pourcentage d'utilisation du CPU"""
    if cpu_percent > 80:
        return "bold red"  # 🔴 Rouge
    elif cpu_percent > 50:
        return "bold orange3"  # 🟠 Orange
    return "bold green"  # 🟢 Vert


def create_display(cpu, memoire, disque, top_processus, temperature, conditions, humidite, bytes_envoyes, bytes_recus):
    """Crée et retourne un Panel contenant l'affichage complet du monitoring."""
    
    # Titre et date/heure
    date_heure = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    titre = Text(f"SYSTÈME DE MONITORING - {date_heure}", style="bold cyan")
    
    # Section Métriques Système
    # Affichage du CPU
    barre_cpu = "█" * int(cpu // 2) + "░" * (50 - int(cpu // 2))
    etat_cpu = "[NORMAL]" if cpu <= 90 else "[CRITIQUE - CPU > 90%]"
    cpu_txt = Text(f"CPU: {barre_cpu} {cpu:.1f}% {etat_cpu}", style="bold")
    
    # Affichage de la mémoire
    barre_memoire = "█" * int(memoire[2] // 2) + "░" * (50 - int(memoire[2] // 2))
    etat_memoire = "[NORMAL]" if memoire[2] < 90 else "[CRITIQUE]"
    memoire_txt = Text(f"MÉMOIRE: {barre_memoire} {memoire[2]:.1f}% (Utilisée: {memoire[0]:.2f} GB / Total: {memoire[1]:.2f} GB) {etat_memoire}", style="bold")
    
    # Tableau de l'espace disque
    table = Table(title="ESPACE DISQUE", show_header=True, header_style="bold magenta")
    table.add_column("Partition", style="cyan")
    table.add_column("Utilisé (GB)", justify="right")
    table.add_column("Total (GB)", justify="right")
    table.add_column("Pourcentage", justify="right")
    for part in disque:
        partition, utilise, total, pourcentage = part
        etat_disque = "[NORMAL]" if pourcentage < 90 else "[CRITIQUE]"
        table.add_row(
            partition,
            f"{utilise:.2f}",
            f"{total:.2f}",
            f"{pourcentage:.1f}% {etat_disque}"
        )
    
    # Section Processus consommant le plus de CPU
    processus_txt = Text("Les processus qui consomment le plus de CPU :", style="bold")
    for idx, p in enumerate(top_processus, 1):
        nom = p.info.get("name", "Inconnu")
        pid = p.info.get("pid", "N/A")
        cpu_proc = p.info.get("cpu_percent", 0)
        mem_info = p.info.get("memory_info")
        mem_proc = mem_info.rss / (1024 ** 2) if mem_info else 0
        cpu_color = get_cpu_color(cpu_proc)  # Appliquer la couleur

        processus_txt.append(f"\n{idx}. {nom} (PID: {pid}) - ", style="bold")
        processus_txt.append(f"{cpu_proc:.1f}% CPU", style=cpu_color)
        processus_txt.append(f" - {mem_proc:.1f} MB MEM")

    # Section Météo
    if temperature is not None:
        etat_temp = "[INFORMATION]" if 10 <= temperature <= 35 else "[ALERTE - Température hors plage]"
        meteo_txt = Text(f"Température: {temperature:.1f}°C - {conditions}\nHumidité: {humidite}% {etat_temp}", style="bold")
    else:
        meteo_txt = Text("Erreur lors de la récupération des données météo.", style="bold red")
    
    # Section Surveillance Réseau
    mo_envoyes = bytes_envoyes / (1024 ** 2)
    mo_recus = bytes_recus / (1024 ** 2)
    reseau_txt = Text(f"Octets envoyés : {mo_envoyes:.2f} Mo | Octets reçus : {mo_recus:.2f} Mo", style="bold")
    
    # Regrouper toutes les sections
    contenu = Group(
        titre,
        cpu_txt,
        memoire_txt,
        table,
        processus_txt,
        Text("-" * 60, style="dim"),
        meteo_txt,
        Text("-" * 60, style="dim"),
        reseau_txt,
        Text("=" * 60, style="dim"),
        Text("Données mises à jour automatiquement toutes les 5 secondes", style="italic"),
        Text("Logs enregistrés dans : logs/", style="italic")
    )
    
    # Retourner le contenu dans un Panel pour une belle bordure
    return Panel(contenu, border_style="green", padding=(1, 2))

if __name__ == "__main__":
    # Exemple de test rapide
    cpu_ex = 78.5
    memoire_ex = (10.9, 16.0, 68.2)
    disque_ex = [("C:\\", 189.2, 298.5, 63.4), ("D:\\", 154.0, 500.0, 30.8)]
    top_processus_ex = []  # Pour tester, la liste peut être vide
    temperature_ex = 24.5
    conditions_ex = "ensoleillé"
    humidite_ex = 45
    bytes_envoyes_ex = 1024 * 1024 * 12  # 12 Mo
    bytes_recus_ex = 1024 * 1024 * 30    # 30 Mo
    panel = create_display(cpu_ex, memoire_ex, disque_ex, top_processus_ex,
                           temperature_ex, conditions_ex, humidite_ex,
                           bytes_envoyes_ex, bytes_recus_ex)
    console.print(panel)
