from django.contrib import admin

# Register your models here.
from .models import Category, Product, Images

class ImageInLine(admin.StackedInline):
    model = Images


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'status']
    list_filter = ['status']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'image_tag']
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    inlines = [ImageInLine]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images)

