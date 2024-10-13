from rich.console import Console
from rich.table import Table
import csv
import os

console = Console()

console.print("Here is some initial data:", style="bold cyan")

table = Table(title="NBA Players")
table.add_column("Name", style="cyan", no_wrap=True)
table.add_column("Height", style="magenta")
table.add_column("Position", justify="center")
table.add_column("Weight", justify="right")

table.add_row("LeBron James", "6'9\"", "SF/PF", "250 lbs")
table.add_row("Stephen Curry", "6'2\"", "PG", "185 lbs")
table.add_row("Giannis Antetokounmpo", "6'11\"", "PF/C", "242 lbs")
table.add_row("Kevin Durant", "6'10\"", "SF/PF", "240 lbs")

console.print(table)
console.print("\n[bold cyan]Now I want you to enter player stats:[/bold cyan]")

players = []

def get_player_data():
    while True:
        name = console.input("Enter the [magenta]name[/magenta] of the player: ")
        height = console.input("Enter the [cyan]height[/cyan] (e.g., 6'7\"): ")
        position = console.input("Enter the [green]position[/green] (e.g., PG, SG, SF): ")
        weight = console.input("Enter the [yellow]weight[/yellow] (in lbs): ")

        console.print("\n[bold]You entered:[/bold]")
        console.print(f"[magenta]Name:[/magenta] {name}")
        console.print(f"[cyan]Height:[/cyan] {height}")
        console.print(f"[green]Position:[/green] {position}")
        console.print(f"[yellow]Weight:[/yellow] {weight} lbs")

        confirm = console.input("\nIs this information correct? ([green]yes[/green]/[red]no[/red]): ").lower()
        if confirm == 'yes':
            return (name, height, position, weight)
        else:
            console.print("[red]Let's try again.[/red]\n")

while True:
    players.append(get_player_data())
    add_more = console.input("\nDo you want to add another player? ([green]yes[/green]/[red]no[/red]): ").lower()
    if add_more != 'yes':
        break

# file path
file_path = os.path.join(os.getcwd(), "players.csv")

# Write to CSV file
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Height", "Position", "Weight"])
    writer.writerows(players)

console.print(f"\n[green]Data has been saved to:[/green] {file_path}")
