from django.contrib import admin
from .models import Book
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'published_date', 'categories', 'average_rating', 'ratings_count', 'thumbnail')
admin.site.register(Book, BookAdmin)