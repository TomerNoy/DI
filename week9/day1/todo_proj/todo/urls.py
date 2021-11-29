from django.urls import path
from . import views

urlpatterns = [
    path('todo_add/', views.TodoCreateView.as_view(), name='todo_add'),
    path('todos/', views.TodoListView.as_view(), name='todos'),
]
