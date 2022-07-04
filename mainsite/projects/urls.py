from django.urls import path
from . import views

urlpatterns = [
    path("",views.projects_index,name='projects_index'),
    path("writing/",views.writing_index,name='writing_index'),
    path("music/",views.music_index,name='music_index'),
    path("<slug:name>", views.album_detail, name='album_detail')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)