from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from .forms import TodoItemForm

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})

def todo_create(request):
    form = TodoItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    return render(request, 'todos/todo_form.html', {'form': form})

def todo_update(request, id):
    todo = get_object_or_404(TodoItem, id=id)
    form = TodoItemForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    return render(request, 'todos/todo_form.html', {'form': form, 'todo': todo})

def todo_delete(request, id):
    todo = get_object_or_404(TodoItem, id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todos/todo_delete.html', {'todo': todo})
