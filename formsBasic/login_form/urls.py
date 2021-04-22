from django.conf.urls import url
from . import views

app_name = 'login_form'


# Be careful setting the name to /login user user_login instead!
urlpatterns =[

    url(r'^relative/$', views.relative, name= 'relative'),
    url(r'^other/$', views.other,name = 'other'),
    url(r'^login_form/$',views.login_form,name="login_form"),
    url(r'^register/$',views.register,name='register'),
    url(r'user_login/$',views.user_login, name='user_login'),

]
