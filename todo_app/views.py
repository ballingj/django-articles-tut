from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm



# Todo List View
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo_app/todo_list.html', {'todos': todos})


# Todo Create View
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo_app/todo_create.html', {'form': form})


# Todo Update View
def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo_app/todo_update.html', {'form': form})


# Todo Delete View
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo_app/todo_delete.html', {'todo': todo})
