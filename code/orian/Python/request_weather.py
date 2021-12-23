import request

import requests
import json 
'''
response = requests.get('https://api.ipify.org', params={'format': 'json'})
print(response.text) # {"ip":"76.105.187.182"} - raw json response
data = response.json() # turn raw json into a python dictionary
print(data) # {'ip': '76.105.187.182'} - python dictionary
print(data['ip']) # 76.105.187.182

import json
data = json.loads(response.text) # use the json library to parse the raw response
print(data) # {'ip': '76.105.187.182'} - python dictionary
print(data['ip']) # 76.105.187.182
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blo
'''
'''
r = requests.get('https://api.openweathermap.org/data/2.5/weather?q={Carson},{WA},{US}&appid={884cfd64f3a52a3354c76c381207cf1e}',params={'format': 'json'})
print(r.text)


r5=requests.get('https://api.openweathermap.org/data/2.5/weather?q=London&appid={af750ce3a6765d0599bf09214bc61f9c}')
par={'format': 'json'}
print(r5)


response = requests.get('https://api.ipify.org',params={'format': 'json'})
print(response.text) # 76.105.187.182
data = response.json()
print(data)
data=json.loads(response.text)
print(data)
print(data['ip'])
'''

we_response = requests.get('https://api.openweathermap.org/data/2.5/weather',zip=98610,us,appid=6a9f2bd2f16f9ba723cc1f8bce51514c)
#data = we_response.json()
print(we_response.text)