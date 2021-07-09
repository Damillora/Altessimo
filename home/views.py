from django.shortcuts import render

import random
from songs.models import Song
from idols.models import Idol

# Create your views here.
def index(request):
    return render(request,"index.html")

def randomizer(request):
    obj = {}
    if "num" in request.GET:
        obj['num'] = request.GET['num']
        song_ids = list(Song.objects.values_list('pk',flat=True))
        song_id = random.choice(song_ids)
        obj['song'] = Song.objects.get(pk=song_id)
        idol_ids = list(Idol.objects.values_list('pk',flat=True))
        idol_selected_ids = random.sample(idol_ids,int(request.GET['num']))
        obj['idols'] = Idol.objects.filter(pk__in=idol_selected_ids)
    return render(request,"randomizer.html",obj)