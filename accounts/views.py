from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from todo.models import Todo  # Ensure this import is correct

# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after signup
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home after login
    return render(request, 'accounts/login.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login after logout

# Home view
@login_required
def home(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todo/index.html', {'username': request.user.username, 'todos': todos})

# API view to fetch todos
@login_required
def get_todos(request):
    todos = Todo.objects.filter(user=request.user).values()
    return JsonResponse(list(todos), safe=False)
