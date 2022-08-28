import requests
from bs4 import BeautifulSoup

tefas_base_url = "https://www.tefas.gov.tr/FonAnaliz.aspx?FonKod="

class DailyFundData:
  """Defines daily fund data scraped from fund's TEFAS analysis page"""

  def __init__(self, code = None, name = None, category = None,
              investor_c = None, piece = None, total_value = None, marketshare = None,
              one_month_p = None, three_month_p = None, six_month_p = None, one_year_p = None,
              price = None, daily_p = None):
    self.code = code
    self.name = name
    self.category = category
    self.investor_c = investor_c
    self.piece = piece
    self.total_value = total_value
    self.marketshare = marketshare
    self.one_month_p = one_month_p
    self.three_month_p = three_month_p
    self.six_month_p = six_month_p
    self.one_year_p = one_year_p
    self.price = price
    self.daily_p = daily_p

  def __str__(self):
    return f'''[{self.code}] {self.name} - {self.category}
{100 * '-'}
{"Yatırımcı Sayısı" : ^20}{"Pay Adedi" : ^20}{"Toplam Değer" : ^20}{"Pazar Payı" : ^20}
{self.investor_c : ^20}{f'{self.piece}' : ^20}{f'₺{self.total_value}' : ^20}{f'%{self.marketshare}' : ^20}

{"Son 1 Ay" : ^20}{"Son 3 Ay" : ^20}{"Son 6 Ay" : ^20}{"Son 1 Yıl" : ^20}
{f'%{self.one_month_p}' : ^20}{f'%{self.three_month_p}' : ^20}{f'%{self.six_month_p}' : ^20}{f'%{self.one_year_p}' : ^20}

{"Bugünkü Fiyat" : ^40}{"Günlük Getiri Yüzdesi" : ^40}
{f'₺{self.price}' : ^40}{f'%{self.daily_p}' : ^40}
'''

# TODO: birden fazla threadde yapılabilir
# TODO: İşlem devam ederken gösterilecek "progress bar" eklenebilir
def get_daily_fund_data(fund_codes):
  fund_data_list = []
  for i in range(len(fund_codes)):
    response = requests.get(tefas_base_url + fund_codes[i])
    content = response.content # we get all the content from the website
    soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
    top_panel = soup.find("ul", class_ = "top-list")
    bottom_panel = soup.find("div", class_= "main-indicators").find("ul").find_next("ul")
    price_panel = soup.find("div", class_ = "price-indicators")

    name = soup.select_one("#MainContent_FormViewMainIndicators_LabelFund").text
    code = fund_codes[i]
    category = top_panel.select_one(":nth-child(5) > span").text
    investor_c = int(bottom_panel.select_one("ul > li:nth-child(2) > span").text.replace('.', ''))
    total_value = float(top_panel.select_one(":nth-child(4) > span").text.replace('.', '').replace(',', '.'))
    marketshare = float(bottom_panel.select_one("ul > li:nth-child(3) > span").text.replace('%', '').replace(',', '.'))
    piece = int(top_panel.select_one(":nth-child(3) > span").text.replace('.', ''))
    price = float(top_panel.select_one(":nth-child(1) > span").text.replace(',', '.'))
    daily_p = float(top_panel.select_one(":nth-child(2) > span").text.replace('%', '').replace(',', '.'))
    one_month_p = float(price_panel.select_one("ul > li:nth-child(1) > span").text.replace('%', '').replace(',', '.'))
    three_month_p = float(price_panel.select_one("ul > li:nth-child(2) > span").text.replace('%', '').replace(',', '.'))
    six_month_p = float(price_panel.select_one("ul > li:nth-child(3) > span").text.replace('%', '').replace(',', '.'))
    one_year_p = float(price_panel.select_one("ul > li:nth-child(4) > span").text.replace('%', '').replace(',', '.'))

    fund_detail = DailyFundData(code, name, category, investor_c, piece, total_value, marketshare, one_month_p, three_month_p, six_month_p, one_year_p, price, daily_p)

    fund_data_list.append(fund_detail)
  return fund_data_list

