from django.shortcuts import render
from projects.models import Collection, Article, Album, Song

# Create your views here.
def home_view(request):
    return render(request, 'projects/home.html')

def projects_index(request):
    collections = Collection.objects.all().order_by('-created_on')
    albums = Album.objects.all().order_by('-created_on')
    context = {
        "collections": collections,
        "album": albums
    }
    return render(request, "projects/projects_index.html", context)

def writing_index(request):
    collections = Collection.objects.all().order_by('-created_on')
    context = {
        "collections": collections
    }
    return render(request, "projects/writing_index.html", context)

def music_index(request):
    albums = Album.objects.all().order_by('-created_on')
    context = {
        "albums": albums
    }
    return render(request, "projects/music_index.html", context)

def album_detail(request, album):
    songs = Song.objects.all().order_by('-created_on').filter(album=album)
    album_obj = Album.objects.get(pk=album)
    context = {
        "album": album_obj
        "songs": songs
    }
    return render(request, "projects/album_detail.html", context)