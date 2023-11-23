from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'year', 'isbn']

admin.site.register(Book)

