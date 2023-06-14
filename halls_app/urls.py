from django.urls import path
from . import views
urlpatterns = [
    path('halls', views.halls),
]