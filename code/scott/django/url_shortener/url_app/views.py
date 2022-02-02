from django.shortcuts import render, redirect
from . models import UrlShortener
from django.utils.crypto import get_random_string
from django.contrib import messages

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def add_url(request):
    if request.method == 'GET':
        return render(request, 'pages/add_url.html')     
    elif request.method == 'POST':
        url_name = request.POST['url'] 
        for x in url_name:
            if 'https://' in url_name:
                messages.warning(request, 'Remove HTTPS:// from the URL')
                return render(request, 'pages/add_url.html')
            else:
                decoded_url = url_name.split('/')
                print('PRINT #1 ',decoded_url)
                random = get_random_string(length=5) 
                url_short = decoded_url[0] + x + '/' + random
                print('PRINT #2 ',url_short)
                UrlShortener.objects.create(url_name = url_name, url_short = url_short)              
                print('LOOK HERE!', url_name)
                return redirect('all')
        
def view_all(request):
  urls = UrlShortener.objects.all()
  return render(request, 'pages/index.html', {'urls': urls})

def update_list(request):
  urls = UrlShortener.objects.all()
  return render(request, 'pages/update_list.html', {'urls': urls})

def delete_url(request, id):
    url = UrlShortener.objects.get(id=id)
    url.delete()
    return redirect('update')