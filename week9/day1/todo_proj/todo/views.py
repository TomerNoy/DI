from django.urls import reverse_lazy
from .forms import AddTodoForm
from .models import *
from django.views.generic import CreateView, ListView


class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todo_add.html'
    form_class = AddTodoForm
    success_url = reverse_lazy('todos')


class TodoListView(ListView):
    model = Todo
    template_name = 'todos.html'
    context_object_name = 'todos'
