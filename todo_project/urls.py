# todo_project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # URL pattern for the Django admin site
    path('admin/', admin.site.urls),
    # URL pattern for including the todo app's URLs
    path('todo/', include('todo_app.urls')),
]

