from scraper import *

#tefas_base_url = "https://www.tefas.gov.tr/FonAnaliz.aspx?FonKod="

fund_codes = ['YAY', 'IPJ', 'MAC']

funds_data_list = get_daily_fund_data(fund_codes)

for fund in funds_data_list:
  print('#' * 100)
  print(fund)
