from django.shortcuts import render, redirect

from .models import Song
# Create your views here.
def song_index(request):
    songs = Song.objects.all()
    return render(request,'songs/index.html',{'songs':songs})

def song_id(request, id):
    song = Song.objects.filter(id=id)[0]
    return redirect(song_show,id=song.id,title=song.title)

def song_show(request, id, title):
    song = Song.objects.filter(id=id,title=title)[0]
    return render(request,'songs/show.html',{'song':song})