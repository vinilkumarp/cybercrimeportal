from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=10,default = '')
    city = models.CharField(max_length=50,default = '')
    subscribe = models.BooleanField(default = False)
    is_admin = models.BooleanField(default = False)
    def __str__(self):
        return self.user.username
        
#creating the userprofile for the superusers
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.get_or_create( user=kwargs['instance'])

post_save.connect( create_profile ,sender=User)
