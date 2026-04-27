from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm 
from django.contrib.auth import authenticate, login, logout 

#boxes.html
def show_boxes(request):
    return render(request, 'boxes.html')

#home.html
def home(request):
    return render(request, 'home.html')
from .forms import SignUpForm 

#sign up.html
def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid(): 
            user = form.save(commit=False) 
            user.set_password(form.cleaned_data['password'])
            user.save() 
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    
    return render(request, 'accounts/signup.html', {'form': form})


#login.html
def login_view(request):
    error = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') # استخدمي الاسم 'home' بدل '/'
            else:
                error = "Invalid username or password"
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form, 'error': error})

#logout.html
def logout_view(request):
    logout(request)
    return redirect('home') 