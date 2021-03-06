from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.FilmsListView.as_view(), name='homepage'),
    path('addFilm/', views.FilmCreateView.as_view(), name='add-film'),
    path('delFilm/<pk>', views.del_film, name='del-film'),
    path('delDirector/<pk>', views.del_director, name='del-director'),
    path('addDirector/', views.DirectorCreateView.as_view(), name='add-director'),
    path('comment/<int:film_id>', views.Comment.as_view(), name='comment-film'),
]
