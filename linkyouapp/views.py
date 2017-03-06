from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from .models import Collection, Link
from .forms import CollectionForm, LinkForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Will be used for user authenticated views
#from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse


# Static pages related views
class Home(TemplateView):
    '''LinkYou homepage with concept description and call to action'''
    def get(self, request):
        return render(request, "home.html")

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
class UserDashboardView(LoginRequiredMixin, TemplateView):
    '''The dashboard of a user and his collections list'''
    # Coming when models exist
    pass


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

class CollectionUpdateView(LoginRequiredMixin, UpdateView):
    '''Update collection view'''
    # Coming when models exist
    pass

class CollectionDeleteView(LoginRequiredMixin, DeleteView):
    '''The delete view yeah'''
    pass

# TODO: The same views as above for links here please and fill them of course
