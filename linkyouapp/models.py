from django.db import models
from django.contrib.auth.models import User  # XXX get_user_model()
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from taggit.managers import TaggableManager

class Collection(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(blank=True, upload_to='uploads/img/collections')
    private = models.BooleanField(default=False)
    tags = TaggableManager()
    user_it_belongs = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
            # Newly created object, so set slug
            self.slug = slugify(self.name)
            super(Collection, self).save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255)
    favorites = models.ManyToManyField(
        Collection,
        through='Favorite',
        through_fields=('profile', 'collection'),
        )

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, *, raw=False, **kwargs):
    if raw:
        return False
    if created:
        Profile.objects.create(user=instance).save()

class Favorite(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile.user.username + " - " + self.collection.name

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
        return self.text

class BlackList(models.Model):
    url= models.URLField(max_length=2000)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.name
