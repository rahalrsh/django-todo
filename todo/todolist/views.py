from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoCreateForm
from django.http import Http404


# Create your views here.
def todo_list_view(request, *args, **kwargs):
    if request.method == 'POST':
        todo_create_form = TodoCreateForm(request.POST)
        if todo_create_form.is_valid():
            todo_create_form.save()

    todos = TodoItem.objects.all()
    todo_create_form = TodoCreateForm()

    context = {
        'todos': todos,
        'todo_create_form': todo_create_form
     }
    return render(request, 'todo_list.html', context)


def todo_update_view(request, todo_id):
    try:
        todo = TodoItem.objects.get(id=todo_id)
    except TodoItem.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        update_form = TodoCreateForm(request.POST, instance=todo)
        if update_form.is_valid():
            update_form.save()
        return redirect('/')

    update_form = TodoCreateForm(instance=todo)

    context = {
        'update_form': update_form,
        'todo': todo
    }
    return render(request, 'todo_update.html', context)


def todo_delete_view(request, todo_id):
    try:
        todo = TodoItem.objects.get(id=todo_id)
    except TodoItem.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        todo.delete()
        return redirect('/')

    context = {
        'todo': todo
    }

    return render(request, 'todo_delete.html', context)

