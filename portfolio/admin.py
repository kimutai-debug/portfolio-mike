# Register your models here.
from django.contrib import admin
from .models import Project
from .models import Contact
admin.site.register(Project)

# portfolio/admin.py
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
