from django.contrib import admin

from apps.models import Project


# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass