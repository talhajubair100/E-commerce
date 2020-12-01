from django.contrib import admin
from .models import Setting
# Register your models here.

class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'update_at', 'status']

admin.site.register(Setting)
