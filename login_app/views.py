from django.shortcuts import render, redirect
from . import models
from halls_app.models import City
from django.contrib import messages

# render the login page
def sign_page(request):
    return render(request, 'login.html')

def register(request):
    errors = models.User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/sign')
    else:
        return models.register_model(request)

def login(request):
    errors = models.User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/sign')
    else:
        return models.login_model(request)


def logout_user(request):
    del request.session['userid']
    return redirect('/')

def logout_admin(request):
    del request.session['adminid']
    return redirect('/')