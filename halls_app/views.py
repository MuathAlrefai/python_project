from django.shortcuts import render, redirect
from . import models

# render the main page
def landing(request):
    
    return render(request, 'landing.html')

def halls(request):
    context = {
        "user": models.get_user_session(request),
    }
    return render(request, 'halls.html', context)

# render the profile page
def profile(request):
    context = {
        "user": models.get_user_session(request),
    }
    return render(request, 'profile.html', context)

# render the admin route
def halls_admin(request):
    context = {
        "user": models.get_user_session(request),
    }
    return render(request, 'admin.html', context)

# render about us page
def about(request):
    return render(request, 'about.html')

# render help page
def help(request):
    return render(request, 'help.html')