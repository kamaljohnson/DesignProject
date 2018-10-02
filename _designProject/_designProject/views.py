from django.shortcuts import render
from django.contrib.auth import logout
def home(request):
    return render(request, 'home.html')

def loginView(request):
    return render(request, 'Registration/login.html')

def logoutView(request):
    logout(request)
    return render(request, 'home.html')
