from django.urls import path
from . import views

urlpatterns = [
    path('sign', views.sign_page),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
]