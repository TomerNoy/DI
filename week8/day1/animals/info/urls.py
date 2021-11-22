from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('animal/<str:id>', views.animal),
    path('family/<str:id>', views.family),
]
