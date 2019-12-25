from django.contrib import admin
from firstapp.models import Client
from firstapp.models import UserProfileInfo,Created_Rooms,Joined_Rooms
# Register your models here.
admin.site.register(Client)
admin.site.register(UserProfileInfo)
admin.site.register(Created_Rooms)
admin.site.register(Joined_Rooms)
