from django.urls import path
from . import views

urlpatterns = [
    path('persons/<str:input>/', views.find_person),
]
