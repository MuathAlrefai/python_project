from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('cities', views.cities),
    path('cities_admin', views.cities_admin),
    path('add_city', views.add_city),
    path('delete_city', views.delete_city),
    path('halls/admin/<city_name>', views.city_halls_admin),
    path('halls/<city_name>', views.city_halls),
    path('halls/admin/<city_name>/<hall_name>', views.hall_info_admin),
    path('halls/<city_name>/<hall_name>', views.hall_info),
    path('halls_admin', views.halls_admin),
    path('halls', views.halls),
    path('add_hall', views.add_hall),
    path('profile', views.profile),
    path('profile_admin', views.profile_admin),
    path('edit_profile_admin', views.edit_profile_admin),
    path('edit_profile', views.edit_profile),
    path('update_profile', views.update_profile),
    path('update_profile_admin', views.update_profile_admin),
    path('change_password', views.change_password),
    path('update_password', views.update_password),
    path('help', views.help),
    path('about', views.about),
    path('book', views.book_hall),
    path('book_success/<hall_name>', views.book_success),
    path('forgot', views.forgot),
]