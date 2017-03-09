from django import forms
from .models import Collection, Link

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = {'name', 'image', 'tags', 'private'}

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = {'url', 'text'}
