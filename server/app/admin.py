from django.contrib import admin
from .models import *

# Register your models here.
class Authoradmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'name']
    search_fields = ['id', 'name']

class Categoryadmin(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields = ['id','name']


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'category', 'publication_date', 'genre', 'isbn', 'cover']
    search_fields = ['title', 'author', 'category', 'isbn']
    list_filter = ['category', 'publication_date']


admin.site.register(Category, Categoryadmin)
admin.site.register(Author, Authoradmin)
admin.site.register(Book, BookAdmin)