from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.utils import timezone

class Article(models.Model):
    STATUS_CHOICES = (
        ("d","Draft"),
        ("p","Publish")
    )
    title = models.CharField(max_length=200,verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="اسلاگ")
    description = models.TextField( verbose_name="توضیحات")
    thumbnail = models.ImageField(upload_to="images", verbose_name="عکس")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateField(auto_now_add=True)
    updated=  models.DateField(auto_now=True)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")

    def thumbnail_show(self):
        return self.thumbnail.url
    
    class Meta:
        verbose_name="مقاله"
        verbose_name_plural="مقالات"
    def __str__(self) -> str:
        return self.title
