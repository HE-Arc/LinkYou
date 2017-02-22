from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login', auth_views.login, name='login'),
    url(r'^logout', auth_views.logout, name='logout'), 
    url(r'^about', views.About.as_view(), name='about'),            # The about page
    url(r'^discover', views.Discover.as_view(), name='discover'),   # The discover collections page
    url(r'^', views.Home.as_view(), name='home'),                   # The homepage
]
