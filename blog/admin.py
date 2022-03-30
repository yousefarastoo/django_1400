from django.contrib import admin
from .models import Article, Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("position", 'title', 'slug', 'status',)
    list_filter = ("title", "status")
    search_fields = (["title","slug"])


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category_to_str','jpublish', 'status',)
    list_filter = ("publish", "status")
    search_fields = ("title", "description")
    ordering = ["status", "-publish"]

    def category_to_str(self,obj):
        return " | ".join([category.title for category in obj.category.all()])
    category_to_str.short_description = "دسته بندی"


admin.site.register(Article, ArticleAdmin)
