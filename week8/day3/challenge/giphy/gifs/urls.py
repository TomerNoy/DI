from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('category/<str:category_name>', views.category, name='category'),
    path('categories/', views.categories, name='categories'),
    path('gif/<int:gif_id>', views.gif_page, name='gif'),
    path('gif/inc/<int:gif_id>', views.inc, name='inc'),
    path('gif/dec/<int:gif_id>', views.dec, name='dec'),
    path('liked', views.liked, name='liked'),
]
