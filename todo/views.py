from django.shortcuts import render, redirect
from .models import Todo
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.


def todo_list(request):
    if request.user.is_authenticated:  # Make sure the user is logged in
        print(f'Current user: {request.user}')
        todos = Todo.objects.filter(user=request.user)  # Only get todos for the logged-in user
        return render(request, 'todo/index.html', {'todos': todos})
    else:
        return redirect('login')  # Redirect to login if the user isn't authenticated


@login_required
def create_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        # Create the todo and assign the logged-in user
        Todo.objects.create(title=title, description=description, user=request.user)
        return redirect('todo_list')
    return render(request, 'todo/create_todo.html')


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
