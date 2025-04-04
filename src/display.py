# src/display.py
from datetime import datetime
from rich.console import Console
from rich.progress import BarColumn, Progress, TextColumn
from rich.table import Table

console = Console()

def display_metrics(cpu, memoire, disque, top_processus, temperature, conditions, humidite):
    """
    Affiche les métriques système et les données météo dans la console.
    
    Arguments:
      cpu          : Pourcentage d'utilisation du CPU.
      memoire      : Tuple (utilisé, disponible, pourcentage) de la mémoire.
      disque       : Liste de tuples (partition, utilisé, total, pourcentage) pour chaque disque.
      top_processus: Liste des processus consommant le plus de CPU.
      temperature  : Température extérieure (None si indisponible).
      conditions   : Description des conditions météorologiques.
      humidite     : Pourcentage d'humidité.
    """
    console.clear()
    date_heure = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    console.print(f"[bold cyan]SYSTÈME DE MONITORING - {date_heure}[/bold cyan]")
    console.print("="*62)
    
    # Affichage des métriques système
    console.print("[bold]--------- MÉTRIQUES SYSTÈME ---------[/bold]")
    
    # CPU
    barre_cpu = "█" * int(cpu // 2) + "░" * (50 - int(cpu // 2))
    etat_cpu = "[NORMAL]" if 10 <= cpu <= 90 else "[CRITIQUE]"
    console.print(f"CPU: {barre_cpu} {cpu}% {etat_cpu}")
    
    # Mémoire
    barre_memoire = "█" * int(memoire[2] // 2) + "░" * (50 - int(memoire[2] // 2))
    etat_memoire = "[NORMAL]" if memoire[2] < 90 else "[CRITIQUE]"
    console.print(f"MÉMOIRE: {barre_memoire} {memoire[2]}% (Utilisé: {memoire[0]:.2f} GB / Total: {memoire[1]:.2f} GB) {etat_memoire}")
    
    # Espace disque
    console.print("ESPACE DISQUE:")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Partition", style="cyan")
    table.add_column("Utilisé (GB)", justify="right")
    table.add_column("Total (GB)", justify="right")
    table.add_column("Pourcentage", justify="right")
    for d in disque:
        etat_disque = "[NORMAL]" if d[3] < 90 else "[CRITIQUE]"
        table.add_row(d[0], f"{d[1]:.2f}", f"{d[2]:.2f}", f"{d[3]}% {etat_disque}")
    console.print(table)
    
    # Top processus
    console.print("[bold]TOP PROCESSUS (CPU):[/bold]")
    for idx, p in enumerate(top_processus, 1):
        nom = p.info.get("name", "Inconnu")
        pid = p.info.get("pid", "N/A")
        cpu_proc = p.info.get("cpu_percent", 0)
        mem_info = p.info.get("memory_info")
        mem_proc = mem_info.rss / (1024 ** 2) if mem_info else 0
        console.print(f"{idx}. {nom} (PID: {pid}) - {cpu_proc}% CPU - {mem_proc:.2f} MB MEM")
    
    # Affichage de la météo
    console.print("[bold]--------- MÉTÉO LOCALE (Paris) ---------[/bold]")
    if temperature is not None:
        etat_temp = "[INFORMATION]" if 10 <= temperature <= 35 else "[WARNING]"
        console.print(f"Température: {temperature}°C - {conditions}\nHumidité: {humidite}% {etat_temp}")
    else:
        console.print("[red]Erreur lors de la récupération des données météo.[/red]")
    
    console.print("="*62)
    console.print("Données mises à jour automatiquement toutes les 5 secondes")
    console.print("Logs enregistrés dans: logs/")

if __name__ == "__main__":
    # Exemple de test rapide
    cpu_ex = 78.5
    memoire_ex = (10.9, 16.0, 68.2)
    disque_ex = [("C:\\", 189.2, 298.5, 63.4), ("D:\\", 154.0, 500.0, 30.8)]
    top_processus_ex = []  # Pour tester, la liste peut être vide
    temperature_ex = 24.5
    conditions_ex = "ensoleillé"
    humidite_ex = 45
    display_metrics(cpu_ex, memoire_ex, disque_ex, top_processus_ex, temperature_ex, conditions_ex, humidite_ex)
