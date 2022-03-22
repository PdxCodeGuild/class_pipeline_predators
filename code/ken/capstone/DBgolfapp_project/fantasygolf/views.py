import imp
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Article, Athlete, User


def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":
        title = request.POST["title"]
        text = request.POST["text"]
        pub_date = request.POST["pub_date"]
        Article.objects.create(title = title, text = text, pub_date = pub_date)
        return redirect('articles')

def get_articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles })

def get_player_card(request):
    athletes = Athlete.objects.all()
    return render(request, 'player.html', {'athletes' : athletes })

def get_league_cards(request):
    return render(request, 'league.html')

def get_profile(request):
    user = request.user
    user_players = Athlete.objects.filter(user = user)
    return render(request, 'profile.html', {'user_players': user_players })

def add_team(request,id):
    if request.method == "GET":
     return render(request, 'player.html')
    elif request.method == "POST":
     user = request.user
     player = Athlete.objects.get(id = id )
     print(player)
     player.user = user
     player.save()
     return redirect('player_card')

def remove_player(request,id):
    player = Athlete.objects.get(id = id)
    print(player)
    team = Athlete.objects.filter(user = request.user)
    print(team)
    #team.delete()
    return redirect('profile')