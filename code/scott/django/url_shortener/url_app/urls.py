from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_all, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('add/', views.add_url, name = 'add_url'),
    path('all/', views.view_all, name = 'all'),
    path('update/', views.update_list, name = 'update'),
    path('delete/<int:id>', views.delete_url, name = 'remove')
]