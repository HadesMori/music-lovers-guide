from collections.abc import Iterable
from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.text import slugify

# Create your models here.

class Band(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, unique=True, editable=False)

    def __str__(self) -> str:
        return self.name
    
    def save(self):
        self.slug = slugify(self.name)
        return super().save()

class Artist(models.Model):
    name = models.CharField(max_length=255)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='artists')

    def __str__(self) -> str:
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='albums', null=True)
    slug = models.SlugField(max_length=255, blank=True, unique=True, editable=False)
    
    def __str__(self) -> str:
        return self.title
    
    def save(self):
        self.slug = slugify(self.title)
        return super().save()

class Song(models.Model):
    title = models.CharField(max_length=255)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='songs')
    year = models.IntegerField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    slug = models.SlugField(max_length=255, blank=True, unique=True, editable=False)

    def __str__(self) -> str:
        return self.title
    
    def save(self):
        self.slug = slugify(self.title)
        return super().save()
    
class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    content = models.TextField(validators=[MinLengthValidator(4)], max_length=400)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="comments")

    def __str__(self) -> str:
        return self.user_name