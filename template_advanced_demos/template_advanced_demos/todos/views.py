from django.shortcuts import render, redirect

from template_advanced_demos.todos.forms import TodoForm
from template_advanced_demos.todos.models import Todo


def list_todos(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todos/list_todos.html', context)


def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list todos')
    else:
        form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'todos/create_todo.html', context)
