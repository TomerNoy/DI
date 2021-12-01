from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.FilmsListView.as_view(), name='homepage'),
    path('addFilm/', views.FilmCreateView.as_view(), name='add-film'),
    path('addDirector/', views.DirectorCreateView.as_view(), name='add-director'),
]
