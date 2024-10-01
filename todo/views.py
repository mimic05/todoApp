from django.shortcuts import render, redirect
from .models import Todo
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos':todos})

def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description  = request.POST.get('description')
        new_todo = Todo.objects.create(title=title, description=description)
        new_todo.save()

    return redirect('todo_list')


# Mark task as complete
def complete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')  # Redirect to the home or the same page

# Delete a task
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('todo_list')  # Redirect to the home or the same page
