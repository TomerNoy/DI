from django.contrib import admin

from .models import Gif
from .models import Category

admin.site.register(Gif)
admin.site.register(Category)

