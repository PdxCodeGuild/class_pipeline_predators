from django.urls import path


from . import views

from django.urls import path

from . import views

urlpatterns = [
    # ex: /fantasygolf/
    # should go to index
    path('index/', views.index, name='index'),
    # says when you type in articles then go to views.py and use method get articles
    path('', views.get_articles, name = 'articles'),
    # when you type in url/fantasygolf/ go to views.py and use the index method 
    path('player/', views.get_player_card, name = 'player_card'),
    # league collection of player cards 
    path('league/', views.get_league_cards, name = 'league_card'),
    #profile
    path('profile/', views.get_profile, name = 'profile'),
    #method for adding team
    path('add/<int:id>', views.add_team, name = 'add')

]