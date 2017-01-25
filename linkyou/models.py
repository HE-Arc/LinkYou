from django.db import models

# Create your models here.
class Link(models.Model):
    url= models.URLField(max_length=2000)
    name = models.CharField(max_length=255)

    def __str__(self):
        return u'%s' % self.name
