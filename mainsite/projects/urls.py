from django.urls import path
from . import views

urlpatterns = [
    path("",views.projects_index,name='projects_index'),
    path("writing/",views.writing_index,name='writing_index'),
    path("music/",views.music_index,name='music_index'),
    path("<slug:name>", views.album_detail, name='album_detail')
]