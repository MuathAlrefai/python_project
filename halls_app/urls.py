from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('halls', views.cities),
    path('halls_admin', views.cities_admin),
    path('profile', views.profile),
    path('admin_profile', views.admin_profile),
    path('edit_profile', views.edit_profile),
    path('update_profile', views.update_profile),
    path('change_password', views.change_password),
    path('update_password', views.update_password),
    path('help', views.help),
    path('about', views.about),
]