from tkinter.font import names

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.home, name='login'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path('project_create/', views.project_create, name='project_create'),
    path('archived_projects/', views.archived_projects, name='archived_projects'),

]