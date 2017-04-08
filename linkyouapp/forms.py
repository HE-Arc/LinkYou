from django import forms
from .models import Collection, Link

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = {'name', 'image', 'tags', 'private'}
        widgets = {
                    'name': forms.TextInput(attrs={'placeholder': 'My great collection'}),
                }

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = {'url', 'text'}
        widgets = {
                    'text': forms.TextInput(attrs={'placeholder': 'My new link'}),
                    'url': forms.TextInput(attrs={'placeholder': 'http://www.example.com'}),
                }
