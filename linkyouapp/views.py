from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView, ListView
from .models import Collection, Link
from django.contrib.auth.models import User
from .forms import CollectionForm, LinkForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from django.http import HttpResponse
from django.urls import reverse


# Static pages related views
class Home(TemplateView):
    '''LinkYou homepage with concept description and call to action'''
    template_name = 'home.html'

    def collections(self):
        return Collection.objects.filter(private=False)


class About(TemplateView):
    '''You know, if we have the time to do it'''
    def get(self, request):
        return render(request, "about.html")

class Discover(TemplateView):
    '''The public page to discover users' collections'''
    template_name = 'discover.html'

    def collections(self):
        return Collection.objects.filter(private=False)


# User related views
class UserDashboardView(LoginRequiredMixin, TemplateView):
    '''The dashboard of a user and his collections list'''
    template_name = "dashboard.html"

    def collections(self):
        return Collection.objects.filter(user_it_belongs=self.request.user)

class UserProfileView(TemplateView):
    template_name = "profile.html"

# Collection related views
class CollectionDetailView(DetailView):
    '''Default view of a collection of links'''
    model = Collection
    template_name = "collection.html"


    def get_queryset(self, *args, **kwargs):
        return Collection.objects.filter(pk=self.kwargs['pk'])

class CollectionCreateView(LoginRequiredMixin, CreateView):
    '''The view of a collection creation'''
    template_name = 'collection_form.html'
    model = Collection
    form_class = CollectionForm

    def form_valid(self, collection_form):
        self.object = collection_form.save(commit=False) # Used by the success_url
        new_collection = collection_form.save(commit=False) # Uncommitted to add creator
        new_collection.user_it_belongs = self.request.user # Add creator (request user)
        new_collection.save() # Final save
        return redirect('new_link', pk=self.object.id, slug=self.object.slug)

    def get_success_url(self):
         return redirect('new_link', pk=self.object.id, slug=self.object.slug)

class CollectionUpdateView(LoginRequiredMixin, UpdateView):
    '''Update collection view'''
    # Coming when models exist
    pass

class CollectionDeleteView(LoginRequiredMixin, DeleteView):
    '''The delete view yeah'''
    pass

# TODO: The same views as above for links here please and fill them of course
class LinkCreateView(LoginRequiredMixin, CreateView):
    '''View of a link creation'''
    template_name = 'link_form.html'
    model = Link
    form_class = LinkForm

    def form_valid(self, LinkForm):
        c = Collection.objects.get(pk=self.kwargs['pk'])

        #self.object = LinkForm.save(commit=False) # Used by the success_url
        new_link = LinkForm.save(commit=False) # Uncommitted to add creator
        new_link.collection_it_belongs = c # Add creator (request user)
        new_link.save() # Final save
        return redirect('dashboard')


    def get_success_url(self):
        return reverse('dashboard')
