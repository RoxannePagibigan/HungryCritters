from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *


def index(request):
    
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        errors = User.objects.RegistrationValidator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return render(request, "register.html")
        else:
            # print(request.POST['password'])
            pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            print(pw_hash)
            newUser = User.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                birthday = request.POST['birthday'],
                email = request.POST['email'],
                password=pw_hash,
            )
            request.session['user'] = newUser.first_name
            request.session['user_email'] = newUser.email
            request.session['user_id'] = newUser.id
            return redirect('/login')
    else:
        return render(request, "register.html")

def login(request):
    if request.method == "POST":
        errors = User.objects.LoginValidator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/login')
        else:
            LoggedUser = User.objects.get(email=request.POST['email'])
            request.session['user'] = LoggedUser.first_name
            request.session['user_email'] = LoggedUser.email
            request.session['user_id'] = LoggedUser.id
            return redirect('/home')            
    else:
        return render(request, "login.html")

def logout(request):
    request.session.flush()
    print(request.session)
    return redirect('/')