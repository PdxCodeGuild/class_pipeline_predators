from django.shortcuts import render, redirect
from .models import Blog


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def blog_posts(request):
    # gets all of the blog posts from the database and store them in a variable
    blogs = Blog.objects.all()

    # creates the context dictionary to send the blog posts to the template
    context = {
        'blogs': blogs
    }
    return render(request, 'pages/posts.html', context)


def add_post(request):
    if request.method == 'GET':  # if its a GET request, just display the add.html template
        return render(request, 'pages/add.html')
    elif request.method == 'POST':  # if it's a POST request ..
        # get the title from the POST submission, this comes from a form
        title = request.POST['title']
        # get the text from the POST submission, this comes from a form
        text = request.POST['text']
        pub_date = request.POST['pub_date']
        # add the new blog post to the database. objects.create() automatically saves the new blog post for us so we
        # don't need a separate call to the save() method
        blogs = Blog.objects.create(title=title, text=text, pub_date=pub_date)
        return redirect('posts')


# we get the id of the element. Remember, all elements are created with an ID in the database.
def see_details(request, id):
    # we are assigning the element to a variable
    post = Blog.objects.get(id=id)
    # we are passing the context to the page
    return render(request, 'pages/details.html', {"post": post})
