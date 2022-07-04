from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='project_images/', null=True)

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    article_file = models.FileField(upload_to='article_files/', null=True)

    def __str__(self):
        return self.title

class Album(models.Model):
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='project_images/', null=True)

class Song(models.Model):
    title = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.title    