# -*- coding: utf-8 -*-
# src/display.py
from datetime import datetime
from rich.console import Console
from rich.table import Table

console = Console()

def display_metrics(cpu, memoire, disque, top_processus, temperature, conditions, humidite, bytes_envoyes, bytes_recus):
    """
    Affiche les métriques système, la météo et la surveillance réseau dans la console.
    
    Arguments:
      cpu            : Pourcentage d'utilisation du CPU.
      memoire        : Tuple (utilisé, disponible, pourcentage) de la mémoire.
      disque         : Liste de tuples (partition, utilisé, total, pourcentage) pour chaque disque.
      top_processus  : Liste des processus consommant le plus de CPU.
      temperature    : Température extérieure (None si indisponible).
      conditions     : Description des conditions météo.
      humidite       : Pourcentage d'humidité.
      bytes_envoyes  : Octets envoyés sur le réseau.
      bytes_recus    : Octets reçus sur le réseau.
    """
    # Affichage du titre avec la date et l'heure
    date_heure = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    console.print(f"[bold cyan]SYSTÈME DE MONITORING - {date_heure}[/bold cyan]")
    console.print("=" * 62)
    
    console.print("[bold]--------- MÉTRIQUES SYSTÈME ---------[/bold]")
    
    # Affichage du CPU avec barre manuelle
    barre_cpu = "█" * int(cpu // 2) + "░" * (50 - int(cpu // 2))
    etat_cpu = "[NORMAL]" if cpu <= 90 else "[CRITIQUE - CPU > 90%]"
    console.print(f"CPU: {barre_cpu} {cpu:.1f}% {etat_cpu}")
    
    # Affichage de la mémoire
    barre_memoire = "█" * int(memoire[2] // 2) + "░" * (50 - int(memoire[2] // 2))
    etat_memoire = "[NORMAL]" if memoire[2] < 90 else "[CRITIQUE]"
    console.print(
        f"MÉMOIRE: {barre_memoire} {memoire[2]:.1f}% "
        f"(Utilisée: {memoire[0]:.2f} GB / Total: {memoire[1]:.2f} GB) {etat_memoire}"
    )
    
    # Affichage de l'espace disque sous forme de tableau
    console.print("ESPACE DISQUE:")
    table = Table(show_header=True, header_style="bold magenta")
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
    console.print(table)
    
    # Affichage des processus consommateurs de CPU
    console.print("[bold]Les processus qui consomment le plus de CPU :[/bold]")
    for idx, p in enumerate(top_processus, 1):
        nom = p.info.get("name", "Inconnu")
        pid = p.info.get("pid", "N/A")
        cpu_proc = p.info.get("cpu_percent", 0)
        mem_info = p.info.get("memory_info")
        mem_proc = mem_info.rss / (1024 ** 2) if mem_info else 0
        console.print(f"{idx}. {nom} (PID: {pid}) - {cpu_proc:.1f}% CPU - {mem_proc:.1f} MB MEM")
    
    # Affichage des données météo
    console.print("[bold]--------- MÉTÉO LOCALE (Paris) ---------[/bold]")
    if temperature is not None:
        etat_temp = "[INFORMATION]" if 10 <= temperature <= 35 else "[ALERTE - Température hors plage]"
        console.print(
            f"Température: {temperature:.1f}°C - {conditions}\nHumidité: {humidite}% {etat_temp}"
        )
    else:
        console.print("[red]Erreur lors de la récupération des données météo.[/red]")
    
    # Affichage de la surveillance réseau
    console.print("[bold]--------- SURVEILLANCE RÉSEAU ---------[/bold]")
    # Conversion en Mo pour une lecture plus aisée
    mo_envoyes = bytes_envoyes / (1024 ** 2)
    mo_recus = bytes_recus / (1024 ** 2)
    console.print(f"Octets envoyés : {mo_envoyes:.2f} Mo | Octets reçus : {mo_recus:.2f} Mo")
    
    console.print("=" * 62)
    console.print("Données mises à jour automatiquement toutes les 5 secondes")
    console.print("Logs enregistrés dans : logs/")
