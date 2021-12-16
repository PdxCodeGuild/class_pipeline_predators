import requests
import json

url = ('https://icanhazdadjoke.com/')

header = {'Accept': 'application/json'}

try:
    
    response = requests.get(url, headers = header) 
except requests.exceptions.RequestException as e:  
    print(e)

dad_joke = response.json()

print(f"Here is your random Dad Joke: {dad_joke['joke']} Hope you enjoyed!")