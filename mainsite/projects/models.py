from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    article_file = models.FileField(upload_to='article_files/', null=True)

    def __str__(self):
        return self.title

class Album(models.Model):
    name = models.CharField(max_length)
    created_on = models.DateTimeField(auto_now=True)
    image = models.ImageField()

class Song(models.Model):
    title = models.CharField(max_length=255)
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.title    