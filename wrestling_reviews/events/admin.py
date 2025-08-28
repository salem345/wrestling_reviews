from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "location", "promotion", "is_ppv", "created_at")
    list_filter = ("promotion", "is_ppv", "date")
    search_fields = ("name", "location", "promotion", "description")
    ordering = ("-date",)

# Register your models here.
