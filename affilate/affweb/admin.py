from django.contrib import admin
from django.contrib.admin import register

from affweb.models import CustomUser


# Register your models here.
@register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass