from django.urls import path
from .views import detail, home

app_name = "blog"

urlpatterns = [
    path('', home, name="home"),
    path('<slug:slug>', detail, name="detail"),
]
