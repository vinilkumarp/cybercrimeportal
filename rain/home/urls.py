from django.urls import path
from .views import view_home
from django.contrib.auth.views import LoginView, LogoutView
 
urlpatterns = [
    path('',view_home,name='view_home'),

]