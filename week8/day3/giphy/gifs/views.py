from django.shortcuts import render
from .models import Gif, Category


def homepage(request):
    gifs = Gif.objects.all()
    return render(request, 'homepage.html', {'gifs': gifs})


def category(request, category_name):
    _category = Category.objects.get(name=category_name)
    print(_category.name, _category.gifs.all())
    gifs = _category.gifs.all()
    return render(request, 'category.html', {'gifs': gifs})


def categories(request):
    _categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': _categories})


def gif(request, gif_id):
    _gif = Gif.objects.get(id=gif_id)
    return render(request, 'gif.html', {'gif': _gif})
