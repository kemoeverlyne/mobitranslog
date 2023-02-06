from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm, ForgotPasswordForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password')
            user = authenticate(username=name, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            # send password reset email
            return redirect('login')
    else:
        form = ForgotPasswordForm()
    return render(request, 'forgot_password.html', {'form': form})

def landing(request):
  slides = [
    {
      'img_src': 'mobitranslog\static\img\1920x1080\01.jpg',
      'title': 'Hi-End Solutions',
      'description': 'Lorem ipsum dolor amet consectetur adipiscing dolore magna aliqua enim minim estudiat veniam siad venumus dolore',
    },
    {
      'img_src': 'img/1920x1080/02.jpg',
      'title': 'Personal Approach',
      'description': 'Lorem ipsum dolor amet consectetur adipiscing dolore magna aliqua enim minim estudiat veniam siad venumus dolore',
    },
  ]
  return render(request, 'landing.html', {'slides': slides})
