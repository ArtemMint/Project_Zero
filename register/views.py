from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

from .forms import UserForm, SignInForm

from django.contrib.auth.models import User


def sign_up_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create(username=username, 
                                       email=email)
            user.set_password(password)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            login(request, user)            
            return redirect('/home/')
    else:
        form = UserForm()
    return render(
        request, 
        'register/sign_up.html',
        {'form': form})

def sign_in_view(request):
    error = ''
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=str(username), password=str(password))
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/home/')
                else:
                    error = "The password is valid, but the account has been disabled!"
            else:
                error = "The username and password were incorrect."
    else:
        form = SignInForm()
    return render(
        request, 
        'register/sign_in.html',
        {'form': form,
        'error': error})

def logout_view(request):
    logout(request)
    return render(
        request, 
        'register/logout.html')
