from django.contrib import admin
from projects.models import Collection, Article, Album, Song

# Register your models here.
class CollectionAdmin(admin.ModelAdmin):
    pass

class ArticleAdmin(admin.ModelAdmin):
    pass

class AlbumAdmin(admin.ModelAdmin):
    pass

class SongAdmin(admin.ModelAdmin):
    pass

admin.site.register(Collection,CollectionAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Album,AlbumAdmin)
admin.site.register(Song,SongAdmin)