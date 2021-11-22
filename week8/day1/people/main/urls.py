from django.urls import path
from . import views

urlpatterns = [
    path('people', views.people),
    path('people/<str:id>', views.person),
]
