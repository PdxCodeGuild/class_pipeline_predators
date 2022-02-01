from tkinter.messagebox import NO, YES
from django.shortcuts import render, redirect
from .models import Todoitem

def home(request):
    return render(request, 'pages/home.html')

def todo_post(request):
    if request.method == 'GET':
        return render(request, 'pages/add.html')
    elif request.method == 'POST':
        created_date = request.POST['created_date']
        text = request.POST['text']
        completed_date = request.POST['completed_date']
        if (request.POST['status'] == 'No'): 
            status = False
        else:
            status = True
        Todoitem.objects.create(created_date = created_date, text = text, completed_date = completed_date, status = status)
        return redirect ('sumary')
        

def sumary(request):
    todos = Todoitem.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'pages/sumary.html', context)

def view(request,id):
    ord = Todoitem.objects.get(id = id)
    context = {
        'ord': ord
    }
    return render(request, 'pages/view.html', context)

def delete_view(request, id):
    ord = Todoitem.objects.get(id =id)
    ord.delete()
    return redirect('sumary')
