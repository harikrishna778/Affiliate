from django.contrib import admin
from django.contrib.admin import register

from crawl.models import Item


# Register your models here.
@register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mrp', 'price', 'discount']
    list_filter = ['discount']
