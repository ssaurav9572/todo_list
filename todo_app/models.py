from django.db import models

# Create your models here.

class TodoItem(models.Model):
    # Define a model for TodoItem
    title = models.CharField(max_length=200)  # Field to store the title of the todo item
    completed = models.BooleanField(default=False)  # Field to store the completion status of the todo item, defaulting to False

    def __str__(self):
        # Define a string representation for TodoItem instances
        return self.title  # Return the title of the todo item when it is converted to a string

