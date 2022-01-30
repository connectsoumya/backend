import django
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .api import *
from django.contrib.auth.models import User
from django.contrib import messages

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

        # Save to Database
        # new_user = User.objects.create_user(username, email, password)
        # new_user.first_name = first_name
        # new_user.last_name = last_name
        # new_user.save()

        messages.success(request, 'Account created successfully')

        return redirect('authentication/sign_in')

    return render(request, 'authentication/create_account.html')

def sign_in(request):
    return render(request, 'authentication/sign_in.html')

def sign_out(request):
    return render(request, 'authentication/sign_out.html')