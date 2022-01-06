from flask import Flask, render_template, request
app = Flask(__name__)
import requests

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city=request.form.get('selected_city')
        state=request.form.get('selected_state')
        try:
            response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city},{state}&units=imperial&appid=884cfd64f3a52a3354c76c381207cf1e')
        except requests.exceptions.RequestException as e:  
            print(e)
        weather_data = response.json()
        location = (weather_data['name'])
        long= (weather_data['coord']['lon'])
        lat= (weather_data['coord']['lat'])
        cur_con = (weather_data['weather'][0]['main'])
        cur_dis = (weather_data['weather'][0]['description'])
        temp = (int(weather_data['main']['temp']))
        feel_temp = (int(weather_data['main']['feels_like']))
        min_temp = (int(weather_data['main']['temp_min']))
        max_temp = (int(weather_data['main']['temp_max']))
        humidity = (weather_data['main']['humidity'])
        wind = (weather_data['wind']['speed'])
        
        print(weather_data)
        return render_template('weather.html', weather_data=weather_data, location=location, 
        long=long, lat=lat, temp=temp, feel_temp=feel_temp, min_temp=min_temp,
        max_temp=max_temp, wind=wind, humidity=humidity, cur_con=cur_con, cur_dis=cur_dis)
    elif request.method == 'GET':
        return 'A GET request was made'
app.run(debug=True)