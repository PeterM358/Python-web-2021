from django.contrib import admin

from template_advanced_demos.todos.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass
