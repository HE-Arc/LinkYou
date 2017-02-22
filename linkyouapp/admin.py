from django.contrib import admin
from django import forms
from .models import Link, Collection

# Register your models here.
class LinkAdminForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = "__all__"

class LinkAdmin(admin.ModelAdmin):
    form = LinkAdminForm

# Register your models here.
class CollectionAdminForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = "__all__"

class CollectionAdmin(admin.ModelAdmin):
    form = CollectionAdminForm

admin.site.register(Link, LinkAdmin)
admin.site.register(Collection, CollectionAdmin)
