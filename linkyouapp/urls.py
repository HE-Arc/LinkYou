from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^collection/new$', views.CollectionCreateView.as_view(), name='new_collection'),
    url(r'^collection/(?P<slug>[\w-]+)-(?P<pk>\d+)$', views.CollectionDetailView.as_view(), name='collection_detail'),
    url(r'^collection/delete/(?P<slug>[\w-]+)-(?P<pk>\d+)$', views.CollectionDeleteView.as_view(), name='delete_collection'),
    url(r'^collection/edit/(?P<slug>[\w-]+)-(?P<pk>\d+)$', views.CollectionUpdateView.as_view(), name='update_collection'),
    url(r'^(?P<pk>\d+)-(?P<slug>[\w-]+)/link/new$', views.LinkCreateView.as_view(), name='new_link'),
    url(r'^favorite/new$', views.CreateFavoriteView.as_view(), name='new_favorite'),
    url(r'^favorite/delete/(?P<pk>\w+)$', views.DeleteFavoriteView.as_view(), name='delete_favorite'),
    url(r'^dashboard$', views.UserDashboardView.as_view(), name='dashboard'),
    url(r'^about$', views.About.as_view(), name='about'),            # The about page
    url(r'^discover$', views.Discover.as_view(), name='discover'),   # The discover collections page
    url(r'^link/edit/(?P<pk>\w+)$', views.LinkUpdateView.as_view(), name='update_link'),
    url(r'^link/delete/(?P<pk>\w+)$', views.LinkDeleteView.as_view(), name='delete_link'),
    url(r'^$', views.Home.as_view(), name='home'),                   # The homepage
]
