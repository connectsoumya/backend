import hashlib
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from api.dynamodbapi import *

# Create your views here.
def home(request):
    # return HttpResponse('Hi, Success')
    return render(request, 'authentication/index.html')

def create_account(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_verify = request.POST.get('password_verify')

        if User.objects.filter(username=username):
            messages.error(request, 'Username already exists')
        elif User.objects.filter(email=email):
            messages.error(request, 'Email already exists')
        elif password != password_verify:
            messages.success(request, 'Passwords do not match. Please try again')
        else:
            password = hashlib.sha256(password.encode())

            # Save to Database
            # new_user = User.objects.create_user(username, email, password)
            # new_user.first_name = first_name
            # new_user.last_name = last_name
            # new_user.save()

            messages.error(request, 'Account created successfully')

            return redirect('/sign_in')

    return render(request, 'authentication/create_account.html')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, 'Wrong username or password')
            return render(request, 'authentication/sign_in.html', {'user': user})
        else:
            login(request, user)
            first_name = user.first_name
            return render(request, 'authentication/index.html', {'first_name': first_name})
            

    return render(request, 'authentication/sign_in.html')

def sign_out(request):
    logout(request)
    return render(request, 'authentication/index.html')