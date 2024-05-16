from django.shortcuts import render
from django.contrib.auth import authenticate as authenticate_user, login as login_user, logout as logout_user
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from UserAuthentication.models import Account


@csrf_exempt
def login(request):
    if request.method == 'POST':
        print(request.POST)
        authenticate = authenticate_user(username=request.POST['username'], password=request.POST['password']) # SELECT * FROM ACCOUNT WHERE USERNAME = USERNAME 
        if authenticate is not None:
            login_user(request, authenticate)
            return JsonResponse({'message': 'Login successful', 'currentUser': request.user.id})
        return JsonResponse({'message': 'Login failed'})

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = request.POST 
        username = data['username']
        password = data['password']
        first_name = data['first_name']
        last_name = data['last_name']
        
        Account.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
        return JsonResponse({'message': 'Registration successful'})