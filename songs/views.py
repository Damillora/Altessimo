from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .models import Song
# Create your views here.
def song_index(request):
    songs = Song.objects.all()
    objs = {}
    if "q" in request.GET:
        q = request.GET['q']
        songs = Song.objects.filter(title__icontains=q) | Song.objects.filter(romanized_title__icontains=q)
        objs['q'] = q
    paginator = Paginator(songs, 100)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    objs['page_obj'] = page_obj
    return render(request,'songs/index.html',objs)

def song_id(request, id):
    song = Song.objects.filter(id=id)[0]
    return redirect(song_show,id=song.id,title=song.title)

def song_show(request, id, title):
    song = Song.objects.filter(id=id,title=title)[0]
    return render(request,'songs/show.html',{'song':song})