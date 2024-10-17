from django.urls import path # type: ignore
from todo import views

urlpatterns = [
    path('complete/<int:todo_id>/', views.complete_todo, name='complete_todo'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('', views.todo_list, name="todo_list"),
    path('home/', views.todo_list, name="todo_list"),
    path('todo/create', views.create_todo, name="create_todo"),
]
 