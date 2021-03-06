from django.db import models
from datetime import datetime
from django.utils import timezone
from accounts.models import User
from django.core.validators import *


class Country(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Film(models.Model):
    title = models.CharField(max_length=60)
    release_date = models.DateField(default=timezone.now)
    created_in_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='categories', blank=True)
    director = models.ManyToManyField(Director, related_name='directors', blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='comments')
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # def get_absolute_url(self):
    #     return reverse('view_post', kwargs={'pk': self.post.id})
