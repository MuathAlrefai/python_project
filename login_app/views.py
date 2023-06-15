from django.shortcuts import render, redirect
from . import models
from halls_app.models import City
from django.contrib import messages

def index(request):
    context = {
        "cities": City.objects.all()
    }
    return render(request, 'index.html', context)

def register(request):
    errors = models.User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/')
    else:
        return models.register_model(request)

def login(request):
    errors = models.User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/')
    else:
        return models.login_model(request)


def logout(request):
    del request.session['userid']
    return redirect('/')