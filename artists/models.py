from django.db import models
from django.apps import apps
from django.utils.text import slugify

# Create your models here.
class ArtistManager(models.Manager):
    def comma_to_qs(self, artists_str):
        final_ids = []
        for artist in artists_str.split(','):
            obj, created = self.get_or_create(romanized_name=artist.strip())
            final_ids.append(obj.id)
        qs = self.get_queryset().filter(id__in=final_ids).distinct()
        return qs

class Artist(models.Model):
    name = models.CharField(max_length=255,blank=True)
    romanized_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,blank=True)
    aliases = models.ManyToManyField("self",blank=True)
    category = models.ManyToManyField("categories.Category",blank=True)
    about_artist = models.TextField(blank=True)
    about_music = models.TextField(blank=True)

    objects = ArtistManager()

    class Meta:
        ordering = [ 'romanized_name','name' ]

    def __str__(self):
        return self.romanized_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.romanized_name)
        super().save(*args,**kwargs)
