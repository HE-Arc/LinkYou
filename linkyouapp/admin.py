from django.contrib import admin
from django import forms
from .models import Link, Collection, Favorite, BlackList, Profile

# Register your models here.
class LinkAdminForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = "__all__"

class LinkAdmin(admin.ModelAdmin):
    form = LinkAdminForm


class CollectionAdminForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = "__all__"

class CollectionAdmin(admin.ModelAdmin):
    form = CollectionAdminForm


class FavoriteAdminForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = "__all__"

class FavoriteAdmin(admin.ModelAdmin):
    form = FavoriteAdminForm

class ProfileAdminForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm

admin.site.register(Link, LinkAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Profile, ProfileAdmin)
