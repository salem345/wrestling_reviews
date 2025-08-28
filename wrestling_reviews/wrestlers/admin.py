from django.contrib import admin
from .models import Wrestler

@admin.register(Wrestler)
class WrestlerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'birth_date','debut_date')  # الأعمدة اللي هتظهر في صفحة المصارعين
    search_fields = ('name', 'country')


# Register your models here.
