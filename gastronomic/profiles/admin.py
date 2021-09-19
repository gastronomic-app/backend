from django.contrib import admin
from django.db import models

from .models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    exclude = ("last_login", )
    list_display=('email','type','is_active')
    list_filter=('is_active','type',)
    search_fields=('email',)
    class meta:
        model = UserProfile


admin.site.register(UserProfile, UserProfileAdmin)
