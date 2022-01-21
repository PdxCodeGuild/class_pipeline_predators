from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_all, name = 'all'),
    path('about/', views.about, name = 'about'),
    path('add/', views.add_item, name = 'add_item'),
    path('all/', views.view_all, name = 'all'),
    path('job_details<int:id>/', views.job_details, name = 'job_details'),
    path('delete/<int:id>', views.delete_job, name = 'remove'),
    path('update/<int:id>', views.update, name = 'update')
]