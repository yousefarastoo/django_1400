from django.urls import path
from .views import detail, home,category_show

app_name = "blog"

urlpatterns = [
    path('', home, name="home"),
    path('<slug:slug>', detail, name="detail"),
    path('category/<slug:slug>', category_show, name="category"),
]
