from django.db import models
from login_app.models import User
import re
import bcrypt

class City(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Hall(models.Model):
    name = models.CharField(max_length=45)
    phone = models.CharField(max_length=10, default=0000000000)
    description = models.TextField()
    capacity = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    # <select>
    # option value="1"> Bad </option>
    # option value="2"> meh </option>
    # option value="3"> neutral </option>
    # option value="4"> good </option>
    # option value="5"> superb </option>
    #1/5 avg = 120/50 = math.ceiling(3.) = 3 
    #hall rating: neutral
    #order by
    # </select>
    city = models.ForeignKey(City, related_name="halls", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="users", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def get_user_session(request):
    return User.objects.get(id=request.session['userid'])

# update user profile model
def update_profile_model(request):
    user = get_user_session(request)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.phone = request.POST['phone']
    user.email = request.POST['email']
    user.save()

# update user password model
def update_password_model(request):
    user = get_user_session(request)
    user.password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    user.save()