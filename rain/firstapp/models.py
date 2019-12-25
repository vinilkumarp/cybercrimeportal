from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #age
    age = models.IntegerField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

class Client(models.Model):
    user_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.user_name



class Created_Rooms(models.Model):
    # User= settings.AUTH_USER_MODEL
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # user= models.ForeignKey(User, null=True)
    name= models.CharField(max_length=500)

class Joined_Rooms(models.Model):
    # User= settings.AUTH_USER_MODEL
    # user= models.ForeignKey(User, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=500)
    def __str__(self):
        return self.user.username
