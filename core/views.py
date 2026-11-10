from django.shortcuts import render

def home(request):
    return render(request, 'accounts/login.html')

def password_reset(request):
    return render(request, 'accounts/login.html')

def register(request):
    return render(request, 'accounts/register.html')