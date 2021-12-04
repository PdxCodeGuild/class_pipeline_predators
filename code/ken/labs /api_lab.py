'''
Visit https://openweathermap.org/price and choose two options within the Free Plan
Build a program that asks the user for a city, and prints out the result. It’s up to you how to build this. 
You can create a loop that asks the user for the current weather, or for a 7 days daily forecast, you can print out the wind speed, convert UTC timestamps in your own local time, etc.
Remember to add a .gitignore file to hide the API key before pushing everything to GitHub!
'''

#API LAB
#activate env ----- source env/bin/activate

#import the function api_key from the file key
from key import api_key

#import requests
import requests

#made key the api key 
keys = api_key()

#Testing if api_key is imported
#print(keys)
#works


#testing lat/long variables 
lat = float(input('what is the lat of your city: '))
long = float(input('what is the long of your city: '))

#Look into params
#pass those answers into the request?
#Use request to GET text from weather api
try:
#added params to turn response into json
  response = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={long}&exclude=hourly,daily&appid={keys}', params={'format': 'json'})
  #Make into Json
  response = response.json()
  #added loads to allow for data to be extracted ----- doesn't work I'd have to import json 
  #response = response.loads(response.text)
  #-----Testing---All-Works------
  #print(response.text) # 76.105.187.182 
  # print(response.url)
  # print(response.text) # 76.105.187.182
  # print(response.status_code) # 200
  # print(response.encoding) # ISO-8859-1
  # print(response.headers) # {'Content-Type': 'text/plain', 'Content-Length': '14', ...}
except requests.exceptions.RequestException as e:
  print(e)


#print the timezone and weather main
#returns a string not calling correctly 
#calling response.text['timezone'] was wrong 
weather = response["timezone"]

#print(weather)

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

