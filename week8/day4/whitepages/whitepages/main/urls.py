from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('persons/<str:input>/', views.find_person, name='person_select'),
    path('find_person', views.find_person_form, name='find_person_form'),
]
