from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='list'),
    path('add/todo', views.add_todo, name='add'),
    path('details/todo', views.details, name='details'),
    path('update/todo', views.update, name='update'),
    path('delete/todo', views.remove_todo, name='remove'),
]
