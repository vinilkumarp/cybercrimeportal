from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100,blank = False)
    phone_no = models.CharField(max_length=100,blank = False, default=' ')
    message =  models.TextField(max_length=2000)
    mail = models.EmailField(max_length=254)
        
    def __str__(self):
        return self.name