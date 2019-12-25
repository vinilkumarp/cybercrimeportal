from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('reg/',views.reg_complaint, name='reg_complaint'),
    path('view/',views.view_complaint,name='view_complaint'),
    path('view-admin/',views.admin_complaint,name = 'admin_complaint'),
    path('post/<int:id>/',views.full_complaint,name='complaint-detail'),
    path('feedbacks/',views.feedbacks,name="feedbacks"),
]