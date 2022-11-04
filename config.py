import requests
from datetime import datetime

BOT_TOKEN = "5761326348:AAHvgH3LXJC-0wJLW0EbAw3rhnxe2h4NWp4"
PRAYER_API = "https://islomapi.uz/api/present/day?region=Toshkent"
REALSOFT = -468956604
# CLASSMATES = -394258396
# TESTGROUP = -818276025
owner_id = 1456374097

def c_hour(): return datetime.now().time().hour

def c_minute(): return datetime.now().time().minute

def get_notify():
    r_data = requests.get(PRAYER_API)
    data = r_data.json()
    today = data['weekday']
    asr = data['times']['asr']
    shom = data['times']['shom_iftor']
    path = None
    if today == 'Juma' and c_hour() == 9 and c_minute() == 5: path = 'Juma.webp'
    elif c_hour() == 13 and c_minute() == 0: path = 'Ctrl_F5.webp'
    elif c_hour() == 13 and c_minute() == 20: path = 'peshin.webp'
    elif c_hour() == int(asr[:2]) and c_minute() == int(asr[3:]): path = 'Ctrl_F5.webp'
    elif c_hour() == int(asr[:2]) and c_minute() == int(asr[3:]) + 7: path = 'asr.webp'
    elif c_hour() == int(shom[:2]) and c_minute() == int(shom[3:]): path = 'Ctrl_F5.webp'
    elif c_hour() == int(shom[:2]) and c_minute() == int(shom[3:]) + 5: path = 'shom.webp'
    return path


# API so'rovlari:
#
# Bugungi namoz vatlarini olish uchun: https://islomapi.uz/api/present/day?region=Toshkent
#
# Shu hafta uchun namoz taqvimi olish uchun: https://islomapi.uz/api/present/week?region=Toshkent
#
# Bir kun uchun namoz taqvimini olish uchun: https://islomapi.uz/api/daily?region=Toshkent&month=4=4&day=5
#
# Bir oylik namoz taqvimini olish uchun: https://islomapi.uz/api/monthly?region=Toshkent&month=4
