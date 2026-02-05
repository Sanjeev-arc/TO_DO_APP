from django.contrib import admin
from todo.models import Task   

# Register your models here.
admin.site.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'category')
    search_fields = ('title', 'category')
    list_filter = ('due_date', 'category')      
    