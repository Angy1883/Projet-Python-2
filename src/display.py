from datetime import datetime
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn
from rich.table import Table

console = Console()

def display_metrics(cpu, memoire, disque, top_processus, temperature, conditions, humidite):
    """
    Affiche les métriques système et les données météo dans la console.
    """
    # On ne fait plus console.clear() ici pour éviter de supprimer l'affichage immédiatement

    date_heure = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    console.print(f"[bold cyan]SYSTÈME DE MONITORING - {date_heure}[/bold cyan]")
    console.print("=" * 62)

    console.print("[bold]--------- MÉTRIQUES SYSTÈME ---------[/bold]")

    # Affichage du CPU (barre "manuelle")
    barre_cpu = "█" * int(cpu // 2) + "░" * (50 - int(cpu // 2))
    etat_cpu = "[NORMAL]" if 10 <= cpu <= 90 else "[CRITIQUE]"
    console.print(f"CPU: {barre_cpu} {cpu:.1f}% {etat_cpu}")

    # Affichage de la mémoire (barre "manuelle")
    barre_memoire = "█" * int(memoire[2] // 2) + "░" * (50 - int(memoire[2] // 2))
    etat_memoire = "[NORMAL]" if memoire[2] < 90 else "[CRITIQUE]"
    console.print(
        f"MÉMOIRE: {barre_memoire} {memoire[2]:.1f}% "
        f"(Utilisée: {memoire[0]:.2f} GB / Total: {memoire[1]:.2f} GB) {etat_memoire}"
    )

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

    console.print("[bold]TOP PROCESSUS (CPU):[/bold]")
    for idx, p in enumerate(top_processus, 1):
        nom = p.info.get("name", "Inconnu")
        pid = p.info.get("pid", "N/A")
        cpu_proc = p.info.get("cpu_percent", 0)
        mem_info = p.info.get("memory_info")
        mem_proc = mem_info.rss / (1024 ** 2) if mem_info else 0
        console.print(f"{idx}. {nom} (PID: {pid}) - {cpu_proc:.1f}% CPU - {mem_proc:.1f} MB MEM")

    console.print(f"[bold]--------- MÉTÉO LOCALE (Paris) ---------[/bold]")
    if temperature is not None:
        etat_temp = "[INFORMATION]" if 10 <= temperature <= 35 else "[WARNING]"
        console.print(
            f"Température: {temperature:.1f}°C - {conditions}\n"
            f"Humidité: {humidite}% {etat_temp}"
        )
    else:
        console.print("[red]Erreur lors de la récupération des données météo.[/red]")

    console.print("=" * 62)
    console.print("Données mises à jour automatiquement toutes les 5 secondes")
    console.print("Logs enregistrés dans: logs/")

