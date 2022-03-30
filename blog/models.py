from django.db import models
from django.utils import timezone
from extensions.utils import jalali_convertor


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="اسلاگ")
    status = models.BooleanField(default=True,verbose_name="وضعیت")
    position = models.IntegerField(verbose_name="پوزیشن")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering=["position"]
    def __str__(self) -> str:
        return self.title

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
    category = models.ManyToManyField(Category,verbose_name="دسته بندی")

    class Meta:
            verbose_name="مقاله"
            verbose_name_plural="مقالات"

    # def thumbnail_show(self):
    #     return self.thumbnail.url
    
    def __str__(self) -> str:
        return self.title
    
    def jpublish(self):
        return jalali_convertor(self.publish)
    jpublish.short_description = "زمان انتشار"
