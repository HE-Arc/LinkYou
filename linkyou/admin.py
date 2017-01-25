from django.contrib import admin
from django import forms
from .models import Link

# Register your models here.
class LinkAdminForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = "__all__"

class LinkAdmin(admin.ModelAdmin):
    form = LinkAdminForm

admin.site.register(Link, LinkAdmin)
