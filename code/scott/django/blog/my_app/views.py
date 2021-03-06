from django.shortcuts import render, redirect
from .models import Author, Article

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def register_author(request): ##if you visit the register/ url, simply render the template
    if request.method == 'GET': 
        return render(request, 'pages/register.html')
    elif request.method == 'POST': ## if you interact with the form on the html page, then get the input from the form and create an instance of the Author class in the database.
        first_name = request.POST['first_name']  
        last_name = request.POST['last_name']    
        email = request.POST['email']
        Author.objects.create(first_name = first_name, last_name = last_name, email = email)
        return redirect('add_posts')

def add_blog_post(request):
    authors = Author.objects.all() ## returns a list of Authors
    context = {'authors': authors} 
    if request.method == 'GET':
        return render(request, 'pages/add_blog_post.html', context) ##passing the list of authors to the page
    elif request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        pub_date = request.POST['pub_date']
        author = Author.objects.get(id=request.POST['author'])
        Article.objects.create(author = author, title = title, text = text, pub_date = pub_date)
        return redirect('view_all')

def view_all(request):
  authors = Author.objects.all()## This queries the database, and saves a list of authors in the variable 'authors'
  return render(request, 'pages/all.html', {'authors': authors})

def post_details(request, id): ##we get the id of the element. Remember, all elements are created with an ID in the database.
    post = Article.objects.get(id = id) ## we are assigning the element to a variable
    return render(request, 'pages/post_details.html', {"post": post})