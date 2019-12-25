from django import forms
from django.contrib.auth.models import User
from firstapp.models import UserProfileInfo
from .models import Client,Created_Rooms,Joined_Rooms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('age','profile_pic')



class clientForm(forms.ModelForm ):
    class Meta:
        model= Client
        fields = '__all__'

class Created_RoomsForm(forms.ModelForm ):
    class Meta:
        model= Created_Rooms
        fields = '__all__'

class Joined_RoomsForm(forms.ModelForm ):
    class Meta:
        model= Joined_Rooms
        fields = '__all__'
