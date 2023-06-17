from django.db import models
from login_app.models import User
import re
import bcrypt

class City(models.Model):
    name = models.CharField(max_length=45)
    image = models.ImageField(upload_to ='city_imgs/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Hall(models.Model):
    name = models.CharField(max_length=45)
    phone = models.CharField(max_length=10, default=0000000000)
    description = models.TextField()
    capacity = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    city = models.ForeignKey(City, related_name="halls", on_delete=models.CASCADE)
    user_booked = models.ManyToManyField(User, related_name="halls_booked")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# get the normal user session object
def get_user_session(request):
    return User.objects.get(id=request.session['userid'])

# get the admin user session object
def get_admin_session(request):
    return User.objects.get(id=request.session['adminid'])

# get all cities
def get_cities_model(request):
    return City.objects.all()

# add a new city
def add_city_model(request):
    city_name = request.POST['city_name']
    city_img = request.POST['city_img']
    City.objects.create(name = city_name, image = city_img)

# update user profile model
def update_profile_model(request):
    user = get_user_session(request)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.phone = request.POST['phone']
    user.email = request.POST['email']
    user.save()

# update admin profile model
def update_profile_admin_model(request):
    admin = get_admin_session(request)
    admin.first_name = request.POST['first_name']
    admin.last_name = request.POST['last_name']
    admin.phone = request.POST['phone']
    admin.email = request.POST['email']
    admin.save()

# get city by name
def get_city_by_name_model(city_name):
    city = City.objects.get(name = city_name)
    return city

# get hall by name
def get_hall_by_name_model(hall_name):
    hall = Hall.objects.get(name = hall_name)
    return hall

# get all halls
def get_halls_model():
    return Hall.objects.all()

# add hall to user's booked halls
def book_hall_model(request):
    user = get_user_session(request)
    hall = request.POST['hall_id']
    hall.user_booked.add(user)

# add a new hall to a city
def add_hall_model(request):
    hall_name = request.POST['hall_name']
    hall_phone = request.POST['hall_phone']
    hall_desc = request.POST['hall_desc']
    hall_capacity = request.POST['hall_capacity']
    hall_rating = request.POST['hall_rating']
    hall_city = City.objects.get(id = int(request.POST['hall_city'])) 
    Hall.objects.create(name = hall_name, phone = hall_phone, description = hall_desc, capacity = hall_capacity, city = hall_city, rating = hall_rating)


# update user password model
def update_password_model(request):
    user = get_user_session(request)
    user.password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    user.save()