from django.conf.urls import url
from firstapp import views

app_name = 'firstapp'

urlpatterns = [

    url(r'^$',views.index,name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^video/$', views.special, name='host'),
    url(r'^chat/comp/$', views.chat, name='host1'),
    url(r'^chat/admin/$', views.chat1, name='host2'),
    url(r'^counsel$', views.counsel, name='host2'),
    


]
