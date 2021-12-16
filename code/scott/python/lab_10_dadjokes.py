import requests
url = ('https://icanhazdadjoke.com/')
headers = {'Accept': 'application/json'}
try:
    response = requests.get(url, headers = headers) 
except requests.exceptions.RequestException as e:  
    print(e)
joke = response.json()
print(f"\nHere is your random Dad Joke: {joke['joke']} Ha Ha!")