from django.db import models
from django.apps import apps

# Create your models here.
class ArtistManager(models.Manager):
    def create_or_new(self, romanized_name):
        romanized_name = romanized_name.strip()
        qs = self.get_queryset().filter(romanized_name__iexact=romanized_name)
        if qs.exists():
            return qs.first(), False
        return Artist.objects.create(romanized_name=romanized_name), True
    
    def comma_to_qs(self, artists_str):
        final_ids = []
        for artist in artists_str.split(','):
            obj, created = self.create_or_new(strip(artist))
            final_ids.append(obj.id)
        qs = self.get_queryset().filter(id__in=final_ids).distinct()
        return qs

class Artist(models.Model):
    name = models.CharField(max_length=255,blank=True)
    romanized_name = models.CharField(max_length=255,blank=True)
    aliases = models.ManyToManyField("self",blank=True)
    category = models.ManyToManyField("categories.Category",blank=True)
    about_composer = models.TextField(blank=True)
    about_music = models.TextField(blank=True)

    objects = ArtistManager()

    class Meta:
        ordering = [ 'romanized_name','name' ]

    def __str__(self):
        return self.romanized_name
