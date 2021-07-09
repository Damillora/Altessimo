from idols.models import Idol
from django.shortcuts import render

# Create your views here.
def idol_index(request):
    idols = Idol.objects.all()
    objs = {}
    if "q" in request.GET:
        q = request.GET['q']
        idols = Idol.objects.filter(name__icontains=q) | Idol.objects.filter(
            romanized_name__icontains=q)
        objs['q'] = q
    objs['idols'] = idols
    return render(request, 'idols/index.html', objs)


def idol_show(request, id):
    idol = Idol.objects.filter(id=id)[0]
    return render(request, 'idols/show.html', {'idol': idol})
