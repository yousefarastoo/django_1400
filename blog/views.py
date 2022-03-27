from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
# Create your views here.

def home(req):
    template_name = "blog/index.html"
    context = {
        "articles":Article.objects.filter(status="p").order_by("-publish")
    }
    return render(req, template_name=template_name,context=context)


def detail(req,slug):
    template_name = "blog/single.html"
    context = { "article":Article.objects.get(slug=slug) }
    return render(request=req,template_name=template_name,context=context)