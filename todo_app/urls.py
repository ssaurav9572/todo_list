# todo_app/urls.py
from django.urls import path
from .views import todo_list, add_todo, delete_todo, toggle_todo

urlpatterns = [
    # URL pattern for the todo list view
    path('', todo_list, name='todo_list'),
    # URL pattern for adding a new todo item
    path('add/', add_todo, name='add_todo'),
    # URL pattern for deleting a todo item
    path('delete/<int:todo_id>/', delete_todo, name='delete_todo'),
    # URL pattern for toggling the completion status of a todo item
    path('toggle/<int:todo_id>/', toggle_todo, name='toggle_todo'),
]

