from django.db import models
from django.contrib.auth.models import User

from tagging.fields import TagField

class Collection(models.Model):
    name= models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length = 200)
    image = models.ImageField()
    likes = models.IntegerField()
    tags = TagField()
    user_it_belongs = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )


    def __str__(self):
        return self.name

class Link(models.Model):
    url= models.URLField(max_length=2000)
    text = models.CharField(max_length=255)
    orderId = models.IntegerField()
    collection_it_belongs = models.ForeignKey(
        'Collection',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.text

class BlackList(models.Model):
    url= models.URLField(max_length=2000)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.name
