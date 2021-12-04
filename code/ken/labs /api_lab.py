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


#pass those answers into the request?
#Use request to GET text from weather api
try:
#added params to turn response into json
  response = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={long}&units=imperial&exclude=hourly,daily&appid={keys}', params={'format': 'json'})
  #Make into Json
  response = response.json()
except requests.exceptions.RequestException as e:
  print(e)


#print the timezone and weather main
#returns a string not calling correctly 
#calling response.text['timezone'] was wrong 
user_city = response["timezone"]
city_weather = response['current']['weather'][0]['description']
city_temp = response['current']['temp']
#print(weather)
#print(city_weather)

#print out weather in city 
print(f'Looks like the weather in {user_city} is {city_weather}')

next_question = input('would you like to know the temp?')

if next_question == 'yes':
  print(f'the current temp for {user_city} is {city_temp} degrees fahrenheit')
  print('thanks byeee')
else:
  print('thanks byeee')




