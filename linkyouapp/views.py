from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView, ListView, View
from .models import Collection, Link, Favorite
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CollectionForm, LinkForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory
from django.db import IntegrityError, transaction
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib import messages


# Static pages related views
class Home(TemplateView):
    '''LinkYou homepage with concept description and call to action'''
    template_name = 'home.html'

    def best_collections(self):
        return Favorite.objects.all()#filter(private=False)

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

    def favorites(self):
        return Favorite.objects.filter(profile=self.request.user.profile)

class UserProfileView(TemplateView):
    template_name = "profile.html"

# Collection related views
class CollectionDetailView(DetailView):
    '''Default view of a collection of links'''
    model = Collection
    template_name = "collection.html"

    def get_context_data(self, **kwargs):
        context = super(CollectionDetailView, self).get_context_data(**kwargs)
        canLike = True
        if self.object.user_it_belongs == self.request.user :
            canLike = False
        if Favorite.objects.filter(collection=self.object, profile=self.request.user.profile):
            canLike = False
        context['canLike']=canLike
        return context

class CollectionCreateView(LoginRequiredMixin, CreateView):
    '''The view of a collection creation'''
    template_name = 'collection_form.html'
    model = Collection
    form_class = CollectionForm

    def form_valid(self, collection_form):
        self.object = collection_form.save(commit=False) # Used by the success_url
        new_collection = collection_form.save(commit=False) # Uncommitted to add creator
        new_collection.user_it_belongs = self.request.user # Add creator (request user)
        new_collection.save()
        collection_form.save_m2m()
        return self.get_success_url()

    def get_success_url(self):
         return redirect('new_link', pk=self.object.id, slug=self.object.slug)

class CollectionUpdateView(LoginRequiredMixin, UpdateView):
    '''Update collection view'''
    model = Collection
    form_class = CollectionForm
    template_name = "collection_form.html"
    success_url = reverse_lazy("dashboard")

class CollectionDeleteView(LoginRequiredMixin, DeleteView):
    '''The delete view yeah'''
    model = Collection
    template_name = "collection_confirm_delete.html"
    success_url = reverse_lazy("dashboard")

class LinkCreateView(LoginRequiredMixin, TemplateView):
    '''View of a link creation'''

    def get(self, request, *args, **kwargs):
        LinkFormSet = formset_factory(LinkForm)

        collection_links = Link.objects.filter(collection_it_belongs=Collection.objects.get(pk=self.kwargs['pk']))
        link_data = [{'text': l.text, 'url': l.url} for l in collection_links]
        link_formset = LinkFormSet(initial=link_data)
        return render(request, 'link_form.html', {'link_formset': link_formset,})

    def post(self, request, *args, **kwargs):
        LinkFormSet = formset_factory(LinkForm)
        link_formset = LinkFormSet(request.POST)
        new_links = []

        if link_formset.is_valid():
            for link_form in link_formset:
                text = link_form.cleaned_data.get('text')
                url = link_form.cleaned_data.get('url')

                if text and url:
                    new_links.append(Link(collection_it_belongs=Collection.objects.get(pk=self.kwargs['pk']), text=text, url=url))

            try:
                with transaction.atomic():
                    Link.objects.filter(collection_it_belongs=Collection.objects.get(pk=self.kwargs['pk'])).delete()
                    Link.objects.bulk_create(new_links)

                    # And notify our users that it worked
                    messages.success(request, 'You have updated your profile.')
                    return HttpResponseRedirect(reverse('collection_detail', kwargs={'pk':int(self.kwargs['pk']), 'slug': 'test'}))

            except IntegrityError: #If the transaction failed
                messages.error(request, 'There was an error saving your profile.')
                return redirect(reverse('profile-settings'))

class CreateFavoriteView(LoginRequiredMixin, View):
    '''Favorite some collection'''

    model = Favorite
    def post(self, request):
        Favorite.objects.create(collection=Collection.objects.get(pk=int(request.POST.get('collection'))),profile=request.user.profile)
        messages.info(request, "Collection liked !")
        return redirect(request.META.get('HTTP_REFERER'))


class LinkUpdateView(LoginRequiredMixin, UpdateView):
    '''Update link view'''
    model = Link
    form_class = LinkForm
    template_name = "link_form_simple.html"
    success_url = reverse_lazy("dashboard")


class LinkDeleteView(LoginRequiredMixin, DeleteView):
    '''The delete form for the view'''
    model = Link
    template_name = "link_confirm_delete.html"

    def get_success_url(self):
        return reverse("collection_detail" , kwargs={"pk":self.object.collection_it_belongs.id, "slug":self.object.collection_it_belongs.slug})
