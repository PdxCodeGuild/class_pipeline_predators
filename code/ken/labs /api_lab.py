
'''
# Requests
The `requests` library allow you to send HTTP requests from a python program, which is the equivalent of typing a url into your browser's address bar and hitting 'enter'. 
You can then receive the data from the website and process it. You can read more in the [official docs](https://requests.readthedocs.io/en/master/) 
and [w3schools](https://www.w3schools.com/python/module_requests.asp).

- [Sending a GET Request](#sending-a-get-request)
- [The Response Object](#the-response-object)
  - [Setting the Encoding](#setting-the-encoding)
- [Specifying Query Parameters](#specifying-query-parameters)
- [Specifying Custom Request Headers](#specifying-custom-request-headers)
- [Receiving JSON](#receiving-json)


## Sending a GET Request

Sending a GET request is the direct equivalent of using your browser, you can get the body of the response using `response.text`.

```python
import requests

response = requests.get('https://api.ipify.org')
print(response.text) # 76.105.187.182
```

## The Response Object

The response object has multiple properties for getting information about the HTTP response. Read more on [w3schools](https://www.w3schools.com/python/ref_requests_response.asp).

```python
import requests

response = requests.get('https://api.ipify.org')
print(response.url)
print(response.text) # 76.105.187.182
print(response.status_code) # 200
print(response.encoding) # ISO-8859-1
print(response.headers) # {'Content-Type': 'text/plain', 'Content-Length': '14', ...}
```

### Setting the Encoding

Depending on the type of response, you may need to set the encoding so the characters are properly interpreted.

```python
import requests
response = requests.get('https://www.gutenberg.org/files/62897/62897-0.txt')
response.encoding = 'utf-8' # set encoding to utf-8
print(response.text)
```


## Specifying Query Parameters

You can use the `params` keyword argument to specify query parameters, which is much cleaner than using string concatenation.

```python
import requests

# cleaner
response = requests.get('https://api.ipify.org', params={'format': 'json'})
print(response.url) # https://api.ipify.org/?format=json

# more messy, especially if you have many query parameters
response = requests.get('https://api.ipify.org?format=json')
```

## Specifying Custom Request Headers

Request headers contain metadata about the request, they can be used to specify an API key or custom user agent.

```python
import requests
response = requests.get('https://api.ipify.org', headers={'User-Agent': 'Mozilla/5.0'})
print(response.text) # 76.105.187.182
```

## Receiving JSON

If the response is in [JSON](../0%20General/09%20-%20JSON,%20CSV,%20&%20XML.md), you can turn it into a python dictionary using the `json.loads()` function or the `json()` method on the response object. You can then extract the relevant data.


```python
import requests
response = requests.get('https://api.ipify.org', params={'format': 'json'})
print(response.text) # {"ip":"76.105.187.182"} - raw json response
data = response.json() # turn raw json into a python dictionary
print(data) # {'ip': '76.105.187.182'} - python dictionary
print(data['ip']) # 76.105.187.182

import json
data = json.loads(response.text) # use the json library to parse the raw response
print(data) # {'ip': '76.105.187.182'} - python dictionary
print(data['ip']) # 76.105.187.182
```

Visit https://openweathermap.org/price and choose two options within the Free Plan
Build a program that asks the user for a city, and prints out the result. It’s up to you how to build this. 
You can create a loop that asks the user for the current weather, or for a 7 days daily forecast, you can print out the wind speed, convert UTC timestamps in your own local time, etc.
This my API Key => 884cfd64f3a52a3354c76c381207cf1e
Remember to add a .gitignore file to hide the API key before pushing everything to GitHub!
'''

#API LAB

#import the function api_key from the file key
from key import api_key

#import requests
import requests

#made key the api key 
keys = api_key()

#Testing if api_key is imported
print(keys)

#Ask the user for the longitude and latidue of the city they want to see
#!!!!!!!!!!!long_city = int(input("Whats the longitude of your city? : "))!!!!!!!!
#!!!!!!!!!!!lat_city = int(input("Whats the lattitude of your city?: "))!!!!!!!!!!


#testing lat/long variables 
lat = 33.44
long = -94.04

#Look into params

#pass those answers into the request?
#Use request to GET text from weather api
try:
#will have to 
  response = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={long}&exclude=hourly,daily&appid={keys}')
  print(response.text) # 76.105.187.182 
  print(response.url)
  print(response.text) # 76.105.187.182
  print(response.status_code) # 200
  print(response.encoding) # ISO-8859-1
  print(response.headers) # {'Content-Type': 'text/plain', 'Content-Length': '14', ...}
except requests.exceptions.RequestException as e:
  print(e)

#test if input works
#!!!!!!!print(first_question)!!!!!!!!! 
#get information for portland and send it back
#!!!!!!!!!!get weather api information!!!!!!!!!!! 
#--------Come back here when done------------
#Got API Key 
#!!!!!!!!!!import API Key here!!!!!!!!!!!!!!
#Then ask if they wanted to see the weather for another location
#Then ask if they want to see another location 
#If they say no quit the program 

