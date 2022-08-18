from django.contrib import admin
from .models import TodoList

class ToDoListAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(TodoList, ToDoListAdmin)