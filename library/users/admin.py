from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'registration_date']

admin.site.register(User)
