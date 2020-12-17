from django.shortcuts import render

# Create your views here.
from .models import Artist
from songs.models import OutsideSong

def artist_index(request):
    artists = Artist.objects.all()
    return render(request,'artists/index.html',{'artists':artists})

def artist_show(request, slug):
    artist = Artist.objects.filter(slug=slug)[0]
    credit_songs = artist.written_songs.all() | artist.composed_songs.all() | artist.arranged_songs.all()
    aliases = artist.aliases.all()
    outside_songs = OutsideSong.objects.filter(composer=artist)
    for alias in aliases:
        credit_songs = credit_songs | alias.written_songs.all() | artist.composed_songs.all() | artist.arranged_songs.all()
        outside_songs = outside_songs | OutsideSong.objects.filter(composer=alias)
    credit_songs = credit_songs.distinct()
    outside_songs = outside_songs.distinct()
    return render(request,'artists/show.html',{'artist': artist,'credit_songs':credit_songs,'outside_songs':outside_songs})