from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from mcmen_dist_app.models import Property
from mcmen_dist_app.models import Driver
from mcmen_dist_app.models import Route
from mcmen_dist_app.models import Article 
#--> Rest
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from .serializers import PropertySerializer
from rest_framework.response import Response
#-->


def landing(request):
    return render(request, 'pages/landing.html')

@login_required
def index(request):
    return render(request, 'pages/index.html')

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('index')
    else:
        messages.warning(request, 'User Name or Password is incorrect')
        return render(request, 'pages/landing.html')

def logout_user(request):
    logout(request)
    return redirect('landing')

def admin_page(request):
    return render(request, 'pages/admin_page.html')

def add_property(request):
    if request.method == 'GET': 
        return render(request, 'pages/add_property.html')
    elif request.method == 'POST': 
        code = request.POST['code']  
        name = request.POST['name']
        phone_num = request.POST['phone_num']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        manager = request.POST['manager']
        brewer = request.POST['brewer']
        delivery = request.POST['delivery']
        notes = request.POST['notes']
        Property.objects.create(code = code, name = name, address = address,
        city = city, state = state, zipcode = zipcode, manager = manager, 
        brewer = brewer, delivery = delivery, notes = notes, phone_num = phone_num)
        return redirect('admin_page')

def add_driver(request):
    if request.method == 'GET': 
        return render(request, 'pages/add_driver.html')
    elif request.method == 'POST': 
        first_name = request.POST['first_name']  
        last_name = request.POST['last_name']
        name = list(last_name)
        nick_name = first_name + '.' + name[0]
        phone_num = request.POST['phone_num']
        Driver.objects.create(first_name = first_name, last_name = last_name, 
        nick_name = nick_name, phone_num = phone_num)
        return redirect('admin_page')

def add_route(request):
    props = Property.objects.all()
    drivers = Driver.objects.all()
    context = {'props': props, 'drivers': drivers}

    if request.method == 'GET':
        return render(request, 'pages/add_route.html', context) 
    elif request.method == 'POST':
        truck_num = request.POST['truck_num']
        # driver = request.POST.getlist('drivers')
        day = request.POST['day']
        mech_record = request.POST['mech_record']
        driver = Driver.objects.get(id=request.POST['drivers'])
        properties = Property.objects.get(id=request.POST['properties'])
        Route.objects.create(truck_num = truck_num, driver = driver, 
        day = day, properties = properties, mech_record = mech_record)
        return redirect('admin_page')

def all_routes(request):
  trucks = Route.objects.all()
  return render(request, 'pages/view_routes.html', {'trucks': trucks})

def all_props(request):
  props = Property.objects.all()
  return render(request, 'pages/view_props.html', {'props': props})

def add_blog_post(request):
    authors = Driver.objects.all()
    context = {'authors': authors} 
    if request.method == 'GET':
        return render(request, 'pages/add_blog_post.html', context) ##passing the list of authors to the page
    elif request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        pub_date = request.POST['pub_date']
        author = Driver.objects.get(id=request.POST['author'])
        Article.objects.create(author = author, title = title, text = text, pub_date = pub_date)
        return redirect('view_all_posts')

def view_all_posts(request):
  articles = Article.objects.all()
  return render(request, 'pages/view_posts.html', {'articles': articles})

def post_details(request, id):
    post = Article.objects.get(id = id)
    return render(request, 'pages/post_details.html', {"post": post})

def prop_details(request, id):
    prop = Property.objects.get(id = id)
    context= {'prop': prop}
    return render(request, 'pages/prop_details.html', context)

@api_view(['GET'])
def property_detail(request, pk, format=None):
    """
    Retrieve a property by id.
    """
    try:
        property = Property.objects.get(pk=pk)
    except Property.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PropertySerializer(property)
        return Response(serializer.data)

# def weather():
#     if request.method == 'POST':
#         city= prop.city
#         state=request.form.get('selected_state')
#         try:
#             response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={prop.city},{prop.state}&units=imperial&appid=884cfd64f3a52a3354c76c381207cf1e')
#         except requests.exceptions.RequestException as e:  
#             print(e)
#         weather_data = response.json()
#         location = (weather_data['name'])
#         long= (weather_data['coord']['lon'])
#         lat= (weather_data['coord']['lat'])
#         cur_con = (weather_data['weather'][0]['main'])
#         cur_dis = (weather_data['weather'][0]['description'])
#         temp = (int(weather_data['main']['temp']))
#         feel_temp = (int(weather_data['main']['feels_like']))
#         min_temp = (int(weather_data['main']['temp_min']))
#         max_temp = (int(weather_data['main']['temp_max']))
#         humidity = (weather_data['main']['humidity'])
#         wind = (weather_data['wind']['speed'])
        
#         return render_template('weather.html', weather_data=weather_data, location=location, 
#         long=long, lat=lat, temp=temp, feel_temp=feel_temp, min_temp=min_temp,
#         max_temp=max_temp, wind=wind, humidity=humidity, cur_con=cur_con, cur_dis=cur_dis)