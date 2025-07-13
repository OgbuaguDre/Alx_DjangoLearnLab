from django.contrib import admin

# Register your models here.
from .models import Book

# Custom Admin Display
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown
    search_fields = ('title', 'author')  # Searchable fields
    list_filter = ('publication_year',)  # Sidebar filter
