from django import forms
from .models import Collection, Link

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = '__all__'

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = '__all__'
