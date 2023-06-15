from django.urls import path
from . import views

urlpatterns = [
    path('halls', views.halls),
    path('profile', views.profile),
    path('halls_admin', views.halls_admin),
]