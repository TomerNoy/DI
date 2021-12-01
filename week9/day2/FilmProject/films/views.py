from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import *
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

from .models import *


class FilmsListView(ListView):
    model = Film
    template_name = 'homepage.html'
    context_object_name = 'films'


class FilmCreateView(CreateView):
    model = Film
    template_name = 'film/addFilm.html'
    form_class = AddFilmForm
    success_url = reverse_lazy('homepage')


class DirectorCreateView(CreateView):
    models = Director
    template_name = 'director/addDirector.html'
    form_class = AddDirectorForm
    success_url = reverse_lazy('homepage')


@user_passes_test(lambda u: u.is_superuser)
def del_film(request, pk):
    film = Film.objects.filter(pk=pk).first()
    messages.success(request, f'film {film.title} was deleted')
    film.delete()
    return redirect('homepage')


@user_passes_test(lambda u: u.is_superuser)
def del_director(request, pk):
    director = Director.objects.filter(pk=pk).first()
    director_name = f'{director.first_name} {director.last_name}'
    messages.success(request, f'director {director_name} was deleted')
    director.delete()
    return redirect('homepage')


class Comment(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content', 'film', 'rating']  # not sure how to define a widget to limit likes 0-5
    template_name = 'posts/post_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        # print('-----', self.kwargs)
        film_id = self.kwargs['film_id']
        print('-----', film_id)
        film = Film.objects.get(id=film_id)
        self.object.film = film
        self.object.save()
        print('---', film)
        return redirect('homepage')
        # return super().form_valid(form)
