from django.shortcuts import render

# Create your views here.


def courses(request): 
    return render(request, 'UserInterface/courses.html')


def login(request): 
    return render(request, 'UserInterface/login.html')