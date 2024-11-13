from django.contrib import admin
from todo_app.models import Todo


# Customizing the Todo admin panels
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
  list_display = ("title", "due_date", "completed")
  ordering = ("due_date", )
  list_filter = ("completed",)
  search_fields = ("title", "description",)
