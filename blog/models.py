from distutils.command.upload import upload
from django.db import models
from django.utils import timezone

class Article(models.Model):
    STATUS_CHOICES = (
        ("d","Draft"),
        ("p","Publish")
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="images")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateField(auto_now_add=True)
    updated=  models.DateField(auto_now=True)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)

    def thumbnail_show(self):
        return self.thumbnail.url
    def __str__(self) -> str:
        return self.title