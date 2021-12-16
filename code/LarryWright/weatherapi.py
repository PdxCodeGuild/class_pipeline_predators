import requests


while True: 
    city = input(' Enter city for location: ')

    weather_description = input(' Would you like a weather description? yes or no: ')

    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=884cfd64f3a52a3354c76c381207cf1e')
    response2 = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat=33.44&lon=-94.04&appid=884cfd64f3a52a3354c76c381207cf1e')

    data = response.json()
    data2 = response2.json()

    print(f'The location of {city} is: ', (data['coord'] ['lon'], data['coord'] ['lat']))

    if weather_description == 'yes':
        print( 'The weather description for today is ', (data2["current"] ["weather"] [0] ["description"]))
    if weather_description != 'yes':
        print(' You have requested no description, have a nice day! ')
    
    choice = print(input('Would you like to continue? y/n: '))

    if choice == 'y or yes':
        continue 
    
    if choice != ' y or yes ' :
        break
    print("goodbye!" )