from django.contrib import admin

from .models import Enterprise, Manager

# Register your models here.


admin.site.register([Enterprise, Manager])
