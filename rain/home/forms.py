from django import forms
from django.db import models
from .models import Feedback
class FeedbackForm(forms.ModelForm):
    mail = forms.EmailField(required=True)
    class Meta:
        model = Feedback
        fields = (
            'phone_no',
            'name',
            'mail',
            'message',
        )