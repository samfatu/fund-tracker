
import sqlite3
from datetime import datetime
from rich.console import Console
import validations

console = Console()

connection = sqlite3.connect('portfolio.db')
c = connection.cursor()

class Transaction:
  def __init__(self, fund_code, lot, cost, date, type):
    self.fund_code = fund_code
    self.lot = lot
    self.cost = cost
    self.date = date
    self.total_cost = round(self.lot * self.cost, 6)
    self.type = type

  def insert_to_db(self):
    with connection:
      if self.type == "buy":
        c.execute("INSERT INTO purchases VALUES (:date, :code, :lot, :cost, :total_cost)",
        {'date': self.date, 'code': self.fund_code, 'lot': self.lot, 'cost': self.cost, 'total_cost': self.total_cost})
      elif self.type == "sell":
        c.execute("INSERT INTO sells VALUES (:date, :code, :lot, :cost, :total_cost)",
        {'date': self.date, 'code': self.fund_code, 'lot': self.lot, 'cost': self.cost, 'total_cost': self.total_cost})

def print_help_in_portfolio():
  print(f'''[bold cyan underline]Komutlar:[/bold cyan underline]
[green][bold]h:[/bold] Yardım
[bold]p:[/bold] Portföyü Görüntüle
[bold]q:[/bold] Çıkış[/green]
  ''')

def prepare_databases():
  create_purchases_db()
  create_sells_db()

def create_purchases_db():
  c.execute('''CREATE TABLE IF NOT EXISTS purchases (
    id integer primary key,
    date text not null,
    code text not null,
    lot integer not null,
    cost real not null,
    total_cost real not null
  )''')
  connection.commit()

def create_sells_db():
  c.execute('''CREATE TABLE IF NOT EXISTS sells (
    id integer primary key,
    date text not null,
    code text not null,
    lot integer not null,
    cost real not null,
    total_cost real not null,
  )''')
  connection.commit()

def fund_transaction(commands):
  with console.status("[bold green]Veritabanına kayıt yapılıyor...") as status:
    if not validations.is_valid_transaction_commands(commands):
      return

    date = datetime.strptime(commands[1], validations.date_format)
    code = commands[2]
    lot = int(commands[3])
    cost = round(float(commands[4]), 6)

    transaction = Transaction(code, lot, cost, date, commands[0])
    transaction.insert_to_db()

def main():
  prepare_databases()
  # Sayfa açılışında portföyü görüntüle
  while True:
    option = input("Portföy > ")

    match option.split(' ')[0]:
      case 'h':
        print("help")
      case 'i':
        print("info")
      case 'p':
        print("Portföyü yazdırır")
      case 'buy':
        fund_transaction(option.split(' '))
      case 'sell':
        fund_transaction(option.split(' '))
      case 'b':
        return
      case _:
        print("Geçersiz komut")