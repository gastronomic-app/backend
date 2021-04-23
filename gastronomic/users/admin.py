from django.contrib import admin

from .models import (
    EstablishmentManager,
    Client,
    Courier
)

# Register your models here.


admin.site.register([EstablishmentManager, Client, Courier])
