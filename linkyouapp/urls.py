from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^about', views.About.as_view(), name='about'),            # The about page
    url(r'^discover', views.Discover.as_view(), name='discover'),   # The discover collections page
    url(r'^', views.Home.as_view(), name='home'),                   # The homepage
]
