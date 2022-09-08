import scraper as sc
import portfolio as p
import sys
from rich import print

fund_codes = ['YAY', 'IPJ', 'MAC']

def main():

  '''Main loop'''
  while True:
    option = input("Ana Menü > ")

    match option.split(' ')[0]:
      case 'h':
        print_help_in_main()
      case 'i':
        open_info(option.split(' '))
      case 'p':
        open_portfolio()
      case 'q':
        print('[bold]Çıkış yapıldı')
        p.connection.close()
        sys.exit()
      case _:
        print("Geçersiz komut")

  # funds_data_list = sc.get_daily_fund_data(fund_codes)

  # for fund in funds_data_list:
  #   print('#' * 100)
  #   print(fund)

def print_help_in_main():
  print(f'''[bold cyan underline]Komutlar:[/bold cyan underline]
[green][bold]h:[/bold] Yardım
[bold]p:[/bold] Portföy
[bold]i:[/bold] Fon Bilgisi
[bold]q:[/bold] Çıkış[/green]
  ''')

def open_portfolio():
  p.main()

def open_info(commands):
  if (len(commands) == 1):
    fund_code = input("Fon kodunu giriniz: ").upper()
  else:
    fund_code = commands[1].upper()

  print(sc.get_daily_fund_data(fund_code))

if __name__ == "__main__":
  main()