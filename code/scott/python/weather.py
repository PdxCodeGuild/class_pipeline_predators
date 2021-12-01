import requests
from s_key import api_key
key = api_key()
print("\nLet's compare the current temperture in two different cities.")
city_name = str(input('\nEnter the first city: '))
city2_name = str(input('\nEnter the second city: '))
try:
   response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&appid={key}')
except requests.exceptions.RequestException as e:  
    print(e)
try:
    response_2 = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city2_name}&units=imperial&appid={key}')
except requests.exceptions.RequestException as e:  
    print(e)
data = response.json()
data_2 = response_2.json()
temp_1 = (int(data['main']['temp'])) 
temp_2 = (int(data_2['main']['temp']))
diff = 0
def temp_diff(a, b):
    if a >= b:
        diff = a-b
    elif b >= a:
        diff = b-a
    return diff
print(f'\n{temp_1}° in {city_name}')
print(f'\n{temp_2}° in {city2_name}')
print(f'\n{temp_diff(temp_1, temp_2)}° is the difference')
