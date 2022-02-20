from django.contrib import admin

from .models import CustomeUsers

# Registered model customeuser in backend admin module
admin.site.register(CustomeUsers)
