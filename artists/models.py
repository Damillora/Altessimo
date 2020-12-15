from django.db import models
from django.apps import apps

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=255)
    romanized_name = models.CharField(max_length=255)
    aliases = models.ManyToManyField("self",blank=True)
    category = models.ManyToManyField("categories.Category",blank=True)
    about_composer = models.TextField(blank=True)
    about_music = models.TextField(blank=True)
    
    def __str__(self):
        return self.romanized_name
