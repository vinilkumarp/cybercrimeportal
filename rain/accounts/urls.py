from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',views.profile, name='profile'),
    path('login/',LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='accounts/logout.html')),
    path('register/',views.register,name = 'register'),
    path('profile/',views.profile, name='profile'),
    path('profile/edit/',views.edit_profile,name='edit_profile'),
    path('change-password/',views.change_password,name='change_password'),
    path('admin/',views.admin_login,name='admin_login'),
    path('validate',views.validation,name='validate'),
    # path('profile/<int:id>/',views.view_profile,name="profile-detail"),
    # path('subscribe/<int:id>/',views.subscribe,name='subscribe'),
    # path('sub-success/',views.sub_success,name='sub-success'),
    # path('test/',views.test_view,name = 'test'),
]