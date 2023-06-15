from django.shortcuts import render, redirect
from . import models

def halls(request):
    context = {
        "user": models.get_user_session(request),
        # "pies": models.get_all_pies(),
    }
    return render(request, 'halls.html', context)

def profile(request):
    context = {
        "user": models.get_user_session(request),
        # "pies": models.get_all_pies(),
    }
    return render(request, 'profile.html', context)

def halls_admin(request):
    context = {
        "user": models.get_user_session(request),
        # "pies": models.get_all_pies(),
    }
    return render(request, 'admin.html', context)

