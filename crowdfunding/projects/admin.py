from django.contrib import admin
from .models import Project, Pledge

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'date_created', 'date_end', 'is_open']
    list_filter = ['is_open', 'date_created', 'date_end']
    search_fields = ['title', 'description']

@admin.register(Pledge)
class PledgeAdmin(admin.ModelAdmin):
    list_display = ['amount', 'supporter', 'project', 'date_created']
    list_filter = ['date_created']
    search_fields = ['comment']

# Register your models here.
