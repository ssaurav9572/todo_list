# todo_app/views.py
from django.shortcuts import render, redirect
from .models import TodoItem

def todo_list(request):
    # Retrieve all TodoItem objects from the database
    todos = TodoItem.objects.all()
    # Render the 'todo_list.html' template with the retrieved todos
    return render(request, 'todo_app/todo_list.html', {'todos': todos})

def add_todo(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Retrieve the title of the new todo from the POST data
        title = request.POST.get('title')
        # Create a new TodoItem with the given title
        TodoItem.objects.create(title=title)
    # Redirect to the 'todo_list' view after adding a todo
    return redirect('todo_list')

def delete_todo(request, todo_id):
    # Retrieve the TodoItem with the specified id from the database
    todo = TodoItem.objects.get(id=todo_id)
    # Delete the retrieved todo
    todo.delete()
    # Redirect to the 'todo_list' view after deleting a todo
    return redirect('todo_list')

def toggle_todo(request, todo_id):
    # Retrieve the TodoItem with the specified id from the database
    todo = TodoItem.objects.get(id=todo_id)
    # Toggle the completion status of the retrieved todo
    todo.completed = not todo.completed
    # Save the changes to the todo
    todo.save()
    # Redirect to the 'todo_list' view after toggling the todo's completion status
    return redirect('todo_list')

