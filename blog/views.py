from unicodedata import category
from django.shortcuts import get_object_or_404, render,get_list_or_404
from django.http import HttpResponse
from .models import Article,Category
# Create your views here.

def home(req):
    template_name = "blog/home.html"
    context = {
        "articles":Article.objects.filter(status="p").order_by("-publish"),
        "category":Category.objects.filter(status = True)
    }
    return render(req, template_name=template_name,context=context)


def detail(req, slug):
    template_name = "blog/detail.html"
    context = {"article": get_object_or_404(Article, slug=slug, status="p")}
    return render(request=req, template_name=template_name, context=context)


def category_show(req, slug):
    template_name = "blog/category.html"
    context = {"category": get_object_or_404(category, slug=slug, status=True)}
    return render(request=req, template_name=template_name, context=context)
