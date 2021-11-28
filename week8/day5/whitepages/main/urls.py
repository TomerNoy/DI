from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_person_form, name='search'),
    # path('persons/<str:input>/', views.find_person),

    path('person/<pk>', views.person, name='person_view'),
    path('search/', views.search_person_form, name='search_person_form_view'),
]
