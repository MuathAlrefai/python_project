from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('halls', views.halls),
    path('halls_admin', views.halls_admin),
    path('profile', views.profile),
    path('help', views.help),
    path('about', views.about),
]