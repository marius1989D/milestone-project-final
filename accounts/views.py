from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.urls import reverse
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm




# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "accounts/index.html")


def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out!')
    return render(request, 'accounts/logout.html')


def login(request):
    """
    This view allow users to log in
    """
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(username=request.POST['username_or_email'],
                                    password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You are loggd in!', extra_tags='alert')
                return redirect('index')
            else:
                user_form.add_error(None, 'Your username or password is incorrect!')
    else:
        user_form = UserLoginForm
    return render(request, 'accounts/login.html', {'user_form': user_form})
    
def register(request):
    """Render the regiastration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
        
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registred")
                return redirect(reverse('index'))
                
            else:
                messages.error(request, "Unable to register your account at this time")
    
    else:
        registration_form = UserRegistrationForm()
        
    return render(request, 'accounts/register.html', {
        "registration_form": registration_form})


@login_required
def profile(request):
    """
    A view that displays the profile page of a logged in user
    """
    return render(request, 'accounts/profile.html')



