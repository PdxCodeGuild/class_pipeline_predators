import requests
import json

def kelvin_to_fahrenheit(kel):
    fah=(((kel-273.15)*1.8)+32)
    fah_round=round(fah,1)
    print(f'{fah_round} °F')#alt 248 + shift F makes the fahrenheit sym for PC.



# ans=kelvin_to_fahrenheit(282.0)


req = requests.get("https://api.openweathermap.org/data/2.5/weather?zip=98610,us&appid=884cfd64f3a52a3354c76c381207cf1e")

data=json.loads(req.text)
# print(data)
# print(data['coord'])
# print(data ['main']['pressure'])
kal_temp1=(data['main']['temp'])
kelvin_to_fahrenheit(kal_temp1)

user_req= input('What zip code do you want to check the temperature at?')

url=(f'https://api.openweathermap.org/data/2.5/weather?zip={user_req},us&appid=884cfd64f3a52a3354c76c381207cf1e')

req= requests.get(url)
data=json.loads(req.text)
temp_k=(data['main']['temp'])
temp_fl=float(temp_k)
kelvin_to_fahrenheit(temp_fl)


