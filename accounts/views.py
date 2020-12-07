from django.shortcuts import render, redirect

from django.contrib.auth import logout


def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    return render(request, 'accounts/register.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
