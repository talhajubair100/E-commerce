from django.contrib import admin
from .models import Setting, ContactMessage
# Register your models here.


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name','subject', 'update_at','status']
    readonly_fields =('name','subject','email','message','ip')
    list_filter = ['status']

class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'update_at', 'status']

admin.site.register(Setting, SettingAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
