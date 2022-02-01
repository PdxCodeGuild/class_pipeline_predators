from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('add/', views.todo_post, name = 'todo_post'),
    path('sumary/', views.sumary, name = 'sumary'),
    path('view/<int:id>', views.view, name = 'view'),
    path('delete/<int:id>', views.delete_view, name = 'delete_view'),
]