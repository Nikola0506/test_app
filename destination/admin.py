# Register your models here.
from django.contrib import admin

from .models import Destination

# Registered model destination in backend admin module
admin.site.register(Destination)
