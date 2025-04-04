from datetime import datetime
from rich.console import Console
from rich.progress import BarColumn, Progress, TextColumn
from rich.table import Table

console = Console()

def display_metrics(cpu, memory, disk, top_processes, temperature, conditions, humidity):
    """
    Affiche les métriques système et les données météo dans la console.
    
    Arguments:
      cpu          : Utilisation CPU (en %)
      memory       : Tuple (used, available, percent) de la mémoire
      disk         : Liste de tuples (device, used, total, percent) pour chaque partition
      top_processes: Liste des processus les plus gourmands en CPU
      temperature  : Température extérieure (peut être None)
      conditions   : Description des conditions météo (peut être None)
      humidity     : Humidité en % (peut être None)
    """
    console.clear()
    # Affichage du titre avec la date et l'heure actuelles
    console.print(f"[bold cyan]SYSTÈME DE MONITORING - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}[/bold cyan]\n")
    
    # Affichage des métriques système
    console.print("[bold]--------- MÉTRIQUES SYSTÈME ---------[/bold]")
    
    # Affichage de l'utilisation CPU avec une barre de progression
    with Progress(
        TextColumn("CPU"),
        BarColumn(),
        TextColumn("{task.percentage:>3.0f}%"),
        console=console, transient=True
    ) as progress:
        progress.add_task("", total=100, completed=cpu)
    
    # Affichage de la mémoire
    with Progress(
        TextColumn("Mémoire"),
        BarColumn(),
        TextColumn("{task.percentage:>3.0f}%"),
        console=console, transient=True
    ) as progress:
        progress.add_task("", total=100, completed=memory[2])
    console.print(f"Utilisée: {memory[0]:.2f} GB, Disponible: {memory[1]:.2f} GB\n")
    
    # Affichage de l'espace disque sous forme de tableau
    table = Table(title="ESPACE DISQUE")
    table.add_column("Partition", justify="center", style="cyan", no_wrap=True)
    table.add_column("Utilisé (GB)", justify="right", style="magenta")
    table.add_column("Total (GB)", justify="right", style="green")
    table.add_column("Pourcentage", justify="right", style="yellow")
    for d in disk:
        table.add_row(d[0], f"{d[1]:.2f}", f"{d[2]:.2f}", f"{d[3]}%")
    console.print(table)
    
    # Affichage des top processus consommant le plus de CPU
    console.print("\n[bold]TOP PROCESSUS (CPU)[/bold]")
    for idx, process in enumerate(top_processes, 1):
        cpu_percent = process.info.get("cpu_percent", 0)
        mem_info = process.info.get("memory_info")
        mem_usage = mem_info.rss / (1024 ** 2) if mem_info else 0
        console.print(f"{idx}. {process.info.get('name', 'Unknown')} (PID: {process.info.get('pid')}) - {cpu_percent}% CPU - {mem_usage:.2f} MB MEM")
    
    # Affichage des données météo
    console.print("\n[bold]--------- MÉTÉO LOCALE ---------[/bold]")
    if temperature is not None:
        console.print(f"Température: {temperature}°C - {conditions} - Humidité: {humidity}%")
        if temperature < 10 or temperature > 35:
            console.print("[red][WARNING] Température extérieure hors plage normale![/red]")
        else:
            console.print("[green]Température dans la plage normale.[/green]")
    else:
        console.print("[red]Erreur de récupération des données météo.[/red]")
    
    # Informations supplémentaires
    console.print("\nDonnées mises à jour automatiquement toutes les 5 secondes")
    console.print("Logs enregistrés dans: logs/")
