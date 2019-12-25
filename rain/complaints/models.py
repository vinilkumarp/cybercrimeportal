from django.db import models
from datetime import datetime 
# from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Complaint(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    category = models.CharField(max_length=100,blank = False)
    # choices=[('Bullying','Bullying'),('Stalking','Stalking'),('Grooming','Grooming'),('Sexting','Sexting'),('Drug','Drug',)])
    date = models.DateTimeField(default = datetime.now(),blank = False)
    description =  models.CharField(max_length=2000)
    image = models.ImageField(upload_to='forum/',default='forum/default.png',blank = True)
    social_media = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.user.username #should be changed

    def get_absolute_url(self):
       return reverse('complaint-detail', kwargs={'id': self.id})
