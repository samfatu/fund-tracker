import sqlite3 as sl

def main():
  # Sayfa açılışında portföyü görüntüle
  while True:
    option = input("Portföy > ")

    match option:
      case 'h':
        print("help")
      case 'i':
        print("info")
      case 'p':
        print("Portföyü yazdırır")
      case 'b':
        return
      case _:
        print("Geçersiz komut")
  pass

def print_help_in_portfolio():
  print(f'''[bold cyan underline]Komutlar:[/bold cyan underline]
[green][bold]h:[/bold] Yardım
[bold]p:[/bold] Portföyü Görüntüle
[bold]q:[/bold] Çıkış[/green]
  ''')