from django.db import models
from login_app.models import User

class City(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Hall(models.Model):
    name = models.CharField(max_length=45)
    phone = models.CharField(max_length=10)
    description = models.TextField()
    capacity = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    city = models.ForeignKey(City, related_name="halls", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="users", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def get_user_session(request):
    return User.objects.get(id=request.session['userid'])