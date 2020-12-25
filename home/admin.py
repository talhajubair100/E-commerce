from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Setting, ContactMessage, FAQ
# Register your models here.


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name','subject', 'update_at','status']
    readonly_fields =('name','subject','email','message','ip')
    list_filter = ['status']

class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'update_at', 'status']

class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'order_number', 'status']
    list_filter = ['status']

admin.site.register(Setting, SettingAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(FAQ, FAQAdmin)
