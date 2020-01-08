from django.contrib import admin
from .models import Scan


@admin.register(Scan)
class ScanAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']

