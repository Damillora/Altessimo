from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .models import Branch, Category
from songs.models import Song
from artists.models import Artist

# Create your views here.
def category_index(request):
    categories = Category.objects.all()
    return render(request,"categories/index.html",{'categories':categories})

def category_show(request, slug):
    category = Category.objects.filter(slug=slug)[0]
    return render(request,"categories/show.html",{'category':category})

def branch_index(request):
    branches = Branch.objects.all()
    return render(request,"branches/index.html",{'branches':branches})

def branch_show(request, acronym):
    branch = Branch.objects.filter(acronym=acronym)[0]
    songs = Song.objects.filter(branch=branch)
    paginator = Paginator(songs, 100)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    return render(request,"branches/show.html",{'branch':branch,'page_obj':page_obj})