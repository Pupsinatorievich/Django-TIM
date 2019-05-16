from django.contrib import admin
from .models import ToDoList
# Register your models here.


class ToDoListAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ToDoList._meta.fields]

    class Meta:
        model = ToDoList

admin.site.register(ToDoList, ToDoListAdmin)