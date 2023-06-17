from django.shortcuts import render, redirect
from . import models
from django.contrib import messages

# render the main page
def landing(request):
    
    return render(request, 'landing.html')

######################## USER PAGES ########################

# render user cities
def cities(request):
    context = {
        "user": models.get_user_session(request),
    }
    return render(request, 'cities.html', context)

# render the user profile page
def profile(request):
    context = {
        "user": models.get_user_session(request),
    }
    return render(request, 'profile.html', context)

# render about us page
def about(request):
    return render(request, 'about.html')

# render help page
def help(request):
    return render(request, 'help.html')

# render edit profile page
def edit_profile(request):
    context = {
        "user": models.get_user_session(request),
    }
    return render(request, 'edit_profile.html', context)

# update profile and redirect to updated profile
def update_profile(request):
    models.update_profile_model(request)
    return redirect('/profile')

# render change user password form
def change_password(request):
    return render(request, 'change_password.html')

# update user password and redirect back to profile page
def update_password(request):
    errors = models.User.objects.password_validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/change_password')
    else:
        models.update_password_model(request)
        return redirect('/profile')
    

######################## ADMIN PAGES ########################

# render the admin route
def cities_admin(request):
    context = {
        "user": models.get_user_session(request),
    }
    return render(request, 'admin_cities.html', context)
