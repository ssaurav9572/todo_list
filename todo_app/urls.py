# todo_app/urls.py
from django.urls import path
from .views import todo_list, add_todo, delete_todo, toggle_todo

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('add/', add_todo, name='add_todo'),
    path('delete/<int:todo_id>/', delete_todo, name='delete_todo'),
    path('toggle/<int:todo_id>/', toggle_todo, name='toggle_todo'),
]
# todo_project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo_app.urls')),
]
