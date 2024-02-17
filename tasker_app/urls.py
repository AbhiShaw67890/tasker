# app/urls.py
from django.contrib import admin
from tasker_app import views
from django.urls import path

# Create your views here.
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('add_user/', views.add_user, name='add_user'),
    path('add_team/', views.add_team, name='add_team'),
    path('assign_task/', views.assign_task, name='assign_task'),
    path('logout/', views.logout_view, name='logout'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
]