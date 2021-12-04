import requests
import time
headers = {'Accept': 'application/json'}
url = 'https://icanhazdadjoke.com'
response = requests.get(url, headers = headers)
data = response.json()
joke = data['joke']
for i in range(0,len(joke)):
    print(joke[i], end='')
    time.sleep(0.1)



headers = {'Accept': 'application/json'}
term = input('what is your sereach term: ')
url = f'https://icanhazdadjoke.com/search?&term={term}'
response = requests.get(url, headers = headers)
data = response.json()
print(f"Total jokes: {data['total_jokes']}")
for i in range(0,len(data['results'])):
    print(data['results'][i]['joke'], end='\n')