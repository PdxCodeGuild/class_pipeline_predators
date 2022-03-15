"""DBgolfapp_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

# I will only use fantasy golf for
#      - Main blog
#      - Fantasy golf 

### ------ ToDo -----###
#   Look into making fantasygolf/ = Home
#### -------------  ####

urlpatterns = [
    # Redirect view kind of works like having '' represent home but what it does is 
    # change the url to append to fantasy golf whenever it is used.
    path('', RedirectView.as_view(url='fantasygolf/', permanent=True)),
    path('fantasygolf/', include('fantasygolf.urls')),
    path('admin/', admin.site.urls),
]
