import imp
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Article


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