from django.urls import path
from . import views

urlpatterns = [
    path('sign', views.sign_page),
    path('register', views.register),
    path('success', views.success),
    path('login', views.login),
    path('logout_user', views.logout_user),
    path('logout_admin', views.logout_admin),
]