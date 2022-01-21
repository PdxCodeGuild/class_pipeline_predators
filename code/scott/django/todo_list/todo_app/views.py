from django.shortcuts import render, redirect
from .models import Todo

def to_do(request):
    return render(request, 'pages/todo_list.html')

def about(request):
    return render(request, 'pages/about.html')

def add_item(request):
    if request.method == 'GET':
        return render(request, 'pages/add_item.html')
    elif request.method == 'POST':
        todo_item = request.POST['todo_item']
        text = request.POST['text']
        create_date = request.POST['create_date']
        finish_date = request.POST['finish_date']
        completed = request.POST['completed']
        print('OVER HERE!', completed)
        Todo.objects.create(todo_item = todo_item, text = text, create_date = create_date, finish_date = finish_date, completed = completed)
        return redirect('all')

def view_all(request):
  jobs = Todo.objects.all()
  return render(request, 'pages/todo_list.html', {'jobs': jobs})

def job_details(request, id): ##we get the id of the element. Remember, all elements are created with an ID in the database.
    job = Todo.objects.get(id = id) ## we are assigning the element to a variable
    return render(request, 'pages/job_details.html', {"job": job})

def delete_job(request, id):
    job = Todo.objects.get(id=id)
    job.delete()
    return redirect('all')

def update(request, id):
    job = Todo.objects.get(id = id)
    if request.method == 'GET':
        return render(request, 'pages/update_item.html', {'job': job})
    elif request.method == 'POST':
        job.todo_item = request.POST['todo_item']
        job.text = request.POST['text']
        job.finish_date = request.POST['finish_date']
        print('LOOK HERE!',job.completed)
    if (request.POST['completed'] == 'False'):
        job.completed = False
    else:
        job.completed = True
    job.save()
    return redirect('all')