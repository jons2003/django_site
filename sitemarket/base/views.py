from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): # HttpRequest
    return HttpResponse("<h1>Главная Страница приложения Маркет</h1>")

def goods(request, good_id):
    return HttpResponse(f"<h1>Страница Товары</h1><h2>{good_id}</h2>")

def goods_by_slug(request, good_slug):
    print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p >slug: {good_slug}</p>")

def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1><p >{year}</p>")