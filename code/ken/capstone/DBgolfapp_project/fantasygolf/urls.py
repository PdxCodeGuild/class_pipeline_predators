from django.urls import path


from . import views

from django.urls import path

from . import views

urlpatterns = [
    # ex: /fantasygolf/
    # should go to index
    path('', views.index, name='index'),
    path('articles/', views.get_articles, name = 'articles' )
    # when you type in url/fantasygolf/ go to views.py and use the index method 
]