from django import forms
from django.db import models
from .models import Complaint
class ComplaintForm(forms.ModelForm):
    image = forms.ImageField(required=True)
    class Meta:
        model = Complaint
        fields = (
            'category',
            'description',
            'image',
            'state',
            'social_media',
        )
