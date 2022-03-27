from re import search
from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", 'title', 'slug', 'publish', 'status',)
    list_filter = ("publish","status")
    search_fields = ("title", "description")
    ordering = ["status","-publish"]

admin.site.register(Article,ArticleAdmin)
