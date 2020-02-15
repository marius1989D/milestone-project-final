from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.urls import reverse
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import UserRegistrationForm, UserLoginForm
from blog.models import Post
from bugs.models import Bug
from features.models import Feature




# Create your views here.
def index(request):
    """Return the index.html file"""
    blogs = Post.objects.filter(status=1).order_by('-created_on')[:6]
    bugs = Bug.objects.order_by('-created_on')[:3]
    features = Feature.objects.order_by('-created_on')[:3]
    
    return render(request, 'index.html', {'blogs': blogs, 'bugs': bugs, 'features': features})

def get_data(request):
    """
    Chart for displaying all Bugs and Features
    """
    labels = ['Features', 'Bugs']
    bugs = Bug.objects.all().count()
    features = Feature.objects.count()
    default = [bugs, features]


    """
    Chart for displaying all Bugs sorted by status
    """
    labels_status_bugs = ['Received', 'In progress', 'Done']
    bugs_received = Bug.objects.filter(status="Received").count()
    bugs_inprogress = Bug.objects.filter(status="In progress").count()
    bugs_done = Bug.objects.filter(status="Done").count()
    default_bugs_status = [bugs_received, bugs_inprogress, bugs_done]

    """
    Chart for displaying all Features sorted by status
    """
    labels_status_features = ['Received', 'In progress', 'Done']
    features_received = Feature.objects.filter(status="Received").count()
    features_inprogress = Feature.objects.filter(status="In progress").count()
    features_done = Feature.objects.filter(status="Done").count()
    default_features_status = [features_received, features_inprogress, features_done]


    data = {
        #chart 1
        "labels": labels,
        "default" : default,

        #chart 2
        "labels_status_bugs": labels_status_bugs,
        "default_bugs_status" : default_bugs_status,

        #chart 3
        "labels_status_features": labels_status_features,
        "default_features_status" : default_features_status,
    }
    return JsonResponse(data)

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




