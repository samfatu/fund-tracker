from datetime import datetime

date_format = "%d.%m.%Y"

def is_valid_buy_commands(commands):
  if (len(commands) != 5):
    print('''Hatalı fon alım komutu girdiniz.'
    Doğru komut formatı: buy TARIH(17.03.2022) FON_KODU(IPJ) ADET(3452) FIYAT(4.123643)''')
    return False

  try:
    date = datetime.strptime(commands[1], date_format)
  except ValueError:
    print("Alım tarihi yanlış formatta girildi. Doğru format: gün.ay.yıl")
    return False

  if (date > datetime.now()):
    print("Alım tarihi bugünden ileri bir tarihte olamaz.")
    return False

  if (len(commands[2]) != 3):
    print("Fon kodu yanlış girildi. Girilen fon kodu 3 harfli olmalıdır.")
    return False

  try:
    int(commands[3])
  except ValueError:
    print("Adet bilgisi yanlış formatta girilmiştir. Değeri tam sayı olarak giriniz.")
    return False

  try:
    float(commands[4])
  except ValueError:
    print("Fiyat bilgisi yanlış formatta girilmiştir. Değerin ondalık kısmını nokta ile ayırarak giriniz.")
    return False

  return True