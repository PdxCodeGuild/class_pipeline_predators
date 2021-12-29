import requests
import json
import time




url='https://icanhazdadjoke.com'
headers={'Accept':'application/json',"User-Agent": "My=library/OR"}
dad_jok=requests.get(headers=headers,url=url)
joke_data=dad_jok.json()
jokes=joke_data['joke']

#print(jokes)
start=input('Do you want to hear a dad joke? ')
n=1

while n == 1:
    if start == "yes":
        print(jokes)
        n=n+1
        time.sleep(3)
        again=input('Do you want to here another joke? ')
    if start == 'no':
        annoy=input('Are you sure?')
        print ('Nice to met you Sure.')
        n=n+1
        break
    
    if again=='yes':
        dad_jok=requests.get(headers=headers,url=url)
        joke_data=dad_jok.json()
        jokes=joke_data['joke']
        print(jokes)
        time.sleep(3)
        ask_2=input('Another joke?')
        
        if ask_2 == 'yes':
            n=1
            dad_jok=requests.get(headers=headers,url=url)
            joke_data=dad_jok.json()
            jokes=joke_data['joke']
            print('ok')
            time.sleep(2)