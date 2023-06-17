from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('cities', views.cities),
    path('cities_admin', views.cities_admin),
    path('add_city', views.add_city),
    path('delete_city', views.delete_city),
    path('profile', views.profile),
    path('profile_admin', views.profile_admin),
    path('edit_profile', views.edit_profile),
    path('update_profile', views.update_profile),
    path('change_password', views.change_password),
    path('update_password', views.update_password),
    path('help', views.help),
    path('about', views.about),
]