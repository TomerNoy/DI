from django.shortcuts import render, redirect
from .models import Gif, Category


def homepage(request):
    gifs = Gif.objects.all()
    return render(request, 'homepage.html', {'gifs': gifs})


def category(request, category_name):
    _category = Category.objects.get(name=category_name)
    print(_category.name, _category.gifs.all())
    gifs = _category.gifs.all()
    return render(request, 'category.html', {'gifs': gifs, 'category': category_name})


def categories(request):
    _categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': _categories})


def gif_page(request, gif_id):
    _gif = Gif.objects.get(id=gif_id)
    return render(request, 'gif.html', {'gif': _gif})


def inc(request, gif_id):
    _gif = Gif.objects.get(id=gif_id)
    _gif.likes = _gif.likes + 1
    _gif.save()
    return redirect('gif', gif_id=gif_id)


def dec(request, gif_id):
    _gif = Gif.objects.get(id=gif_id)
    _gif.likes = _gif.likes - 1
    _gif.save()
    return redirect('gif', gif_id=gif_id)


def liked(request):
    _liked = Gif.objects.filter(likes__gt=1).order_by('likes').reverse()
    return render(request, 'liked.html', {'liked': _liked})
