# Register your models here.
from django.contrib import admin

from .models import Trip

# Registered model trip in backend admin module
admin.site.register(Trip)
