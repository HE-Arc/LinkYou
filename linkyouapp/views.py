from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView, ListView
from .models import Collection, Link
from django.contrib.auth.models import User
from .forms import CollectionForm, LinkForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Will be used for user authenticated views
#from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse
from django.urls import reverse


# Static pages related views
class Home(ListView):
    '''LinkYou homepage with concept description and call to action'''
    context_object_name = 'featured_collection_list'
    queryset = Collection.objects.order_by("-pk")[:3] #  TODO: filter featured = True ou most liked ?
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)      # Le contexte de base defini au dessus
        context['last_collection_list'] = Collection.objects.order_by("-pk")[:4] # Un ajout pour avoir les dernieres collections
        context['last_users_list'] = User.objects.order_by("-pk")[:5]  # Un ajout pour avoir les derniers utilisateurs
        return context


class About(TemplateView):
    '''You know, if we have the time to do it'''
    def get(self, request):
        return render(request, "about.html")

class Discover(TemplateView):
    '''The public page to discover users' collections'''
    def get(self, request):
        context = {}
        context["collections"] = ["Collection 1", "Collection 2", "Collection 3", "Collection 4", "Collection 5"]
        return render(request, "discover.html", context)


# User related views
class UserDashboardView(LoginRequiredMixin, ListView):
    '''The dashboard of a user and his collections list'''
    context_object_name = 'user_collections_list'
    template_name = 'dashboard.html'

    def get_queryset(self):
        return Collection.objects.filter(user_it_belongs=self.request.user)

class UserProfileView(TemplateView):
    def get(self, request):
        return render(request, "profile.html")

# Collection related views
class CollectionDetailView(DetailView):
    '''Default view of a collection of links'''
    # Coming when models exist
    pass

class CollectionCreateView(LoginRequiredMixin, CreateView):
    '''The view of a collection creation'''
    template_name = 'collection_form.html'
    model = Collection
    form_class = CollectionForm

    def get_success_url(self):
         return reverse('dashboard')

class CollectionUpdateView(LoginRequiredMixin, UpdateView):
    '''Update collection view'''
    # Coming when models exist
    pass

class CollectionDeleteView(LoginRequiredMixin, DeleteView):
    '''The delete view yeah'''
    pass

# TODO: The same views as above for links here please and fill them of course
