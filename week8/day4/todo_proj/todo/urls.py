from django.urls import path

from . import views

urlpatterns = [
    path('todo_add/', views.todo_add_view, name='todo_add'),
    path('todos/', views.todos_view, name='todos'),
]
