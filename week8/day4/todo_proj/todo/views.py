from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Category, Todo


def todo_add_view(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            Todo.objects.create(**form.cleaned_data)
            return redirect('todos')

    if request.method == 'GET':
        form = TodoForm()
    return render(request, 'todo_add.html', {'form': form})


def todos_view(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'todos.html', context)
