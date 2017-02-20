from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

from django.http import HttpResponse


class Home(TemplateView):
    '''LinkYou homepage with concept description and call to action'''
    def get(self, request):
        return render(request, "home.html")
