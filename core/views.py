from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
import logging

def home(request):
    if request.user.is_authenticated:
        redirect('dashboard')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            logging.info('user logged in')
            django_login(request, user)
            return redirect("dashboard")

    return render(request, 'accounts/login.html')

def password_reset(request):
    return render(request, 'accounts/login.html')

def register(request):
    return render(request, 'accounts/register.html')

def logout(request):
    if request.user.is_authenticated:
        django_logout(request)

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'projects/dashboard.html')
    return redirect('home')

def project_create(request):
    if request.method == 'POST':
        return None
    return None

def archived_projects(request):
    if request.method == 'POST':
        return None
    return None