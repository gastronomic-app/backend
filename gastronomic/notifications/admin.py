from django.contrib import admin

from .models import Notification

# Register your models here.


@admin.register(Notification)
class orderAdmin(admin.ModelAdmin):
    list_display=('title', 'message', 'created')
