from django.db import models
from django.contrib.auth.models import User


class Collection(models.Model):
    name= models.CharField(max_length=255)
    icon = models.URLField(max_length=2000)
    slug = models.SlugField(unique=True, max_length = 200)
    user_it_belongs = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )


    def __str__(self):
        return u'%s' % self.name

class Link(models.Model):
    url= models.URLField(max_length=2000)
    text = models.CharField(max_length=255)
    collection_it_belongs = models.ForeignKey(
        'Collection',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    def __str__(self):
        return u'%s' % self.text
