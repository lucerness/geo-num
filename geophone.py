import json
import requests
import pyfiglet
icon = pyfiglet.figlet_format("geo-numbers")
print(icon)
numberget = int(input('введите номер телефона : \n'))
class Search:
    global phonenumbers
    phonenumbers = numberget
    def phonesearch(phone=phonenumbers):
        try:
          response = requests.get(f'https://mobile-tracker.biz/emulator/check?driver=geo&country=RU&provider=phone&uid=+{phone}&mode=undefined&_=1648381248958')
          decode_text = json.loads(response.text)
          location = decode_text.get('location')
          geo_city = location.get('geo_city')
          print('Координаты', phonenumbers, geo_city)

        except Exception as exp:
            print(exp)

Search.phonesearch()
