from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=255)
    romanized_title = models.CharField(max_length=255)
    lyricist = models.ManyToManyField("artists.Artist", blank=True, related_name="written_songs")
    composer = models.ManyToManyField("artists.Artist", blank=True, related_name="composed_songs")
    arranger = models.ManyToManyField("artists.Artist", blank=True, related_name="arranged_songs")
    impression = models.TextField(blank=True)

class OutsideSong(models.Model):
    title = models.CharField(max_length=255)
    romanized_title = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    composer = models.ForeignKey("artists.Artist", blank=True, on_delete=models.CASCADE)
