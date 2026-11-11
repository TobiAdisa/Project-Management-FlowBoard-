from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout

def home(request):
    if request.user.is_authenticated:
        return render(request, 'projects/dashboard.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            return redirect("projects:dashboard")

    return render(request, 'accounts/login.html')

def password_reset(request):
    return render(request, 'accounts/login.html')

def register(request):
    return render(request, 'accounts/register.html')

def logout(request):
    if request.user.is_authenticated:
        django_logout(request)

def project_create(request):
    if request.method == 'POST':
        return None
    return None

def archived_projects(request):
    if request.method == 'POST':
        return None
    return None