from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^accounts/',include('registration.backends.simple.urls'), name='registration_register'),
    url(r'^collection/new', views.CollectionCreateView.as_view(), name='new_collection'),
    url(r'^collection/(?P<slug>[\w-]+)-(?P<pk>\w+)', views.CollectionDetailView.as_view(), name='collection_detail'),
    url(r'^collection/delete/(?P<slug>[\w-]+)-(?P<pk>\w+)', views.CollectionDeleteView.as_view(), name='delete_collection'),
    url(r'^collection/edit/(?P<slug>[\w-]+)-(?P<pk>\w+)', views.CollectionUpdateView.as_view(), name='update_collection'),
    url(r'^(?P<pk>\w+)-(?P<slug>[\w-]+)/link/new', views.LinkCreateView.as_view(), name='new_link'),
    url(r'^favorite/new', views.CreateFavoriteView.as_view(), name='new_favorite'),
    url(r'^login', auth_views.login, name='login'),
    url(r'^logout', auth_views.logout, name='logout'),
    url(r'^dashboard', views.UserDashboardView.as_view(), name='dashboard'),
    url(r'^about', views.About.as_view(), name='about'),            # The about page
    url(r'^discover', views.Discover.as_view(), name='discover'),   # The discover collections page
    url(r'^link/edit/(?P<pk>\w+)', views.LinkUpdateView.as_view(), name='update_link'),
    url(r'^link/delete/(?P<pk>\w+)', views.LinkDeleteView.as_view(), name='delete_link'),
    url(r'^', views.Home.as_view(), name='home'),                   # The homepage
]
