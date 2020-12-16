from django.db import models


# Create your models here.
class Song(models.Model):
    branch = models.ForeignKey("categories.Branch", on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    romanized_title = models.CharField(max_length=255,blank=True)
    lyricist = models.ManyToManyField("artists.Artist", blank=True, related_name="written_songs")
    composer = models.ManyToManyField("artists.Artist", blank=True, related_name="composed_songs")
    arranger = models.ManyToManyField("artists.Artist", blank=True, related_name="arranged_songs")
    impression = models.TextField(blank=True)

    class Meta:
        ordering = [ 'romanized_title','title' ]  

    def __str__(self):
        return "["+self.branch.acronym+"] "+self.title

class OutsideSong(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255,blank=True)
    origin = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    composer = models.ForeignKey("artists.Artist", blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = [ 'composer','title' ]  

    def __str__(self):
        return "["+self.composer.romanized_name+"] "+self.title
