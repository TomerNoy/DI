from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import *
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

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
