from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ForeignKey('Image', related_name='thumbnail_of')


class Image(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    album = models.ForeignKey(Album)
    file = models.ImageField()