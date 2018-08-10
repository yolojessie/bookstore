from django.contrib import admin
from book.models import Book
# Register your models here.
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['bkName','authorName','publisher','pubversion','price']
    list_display_links = ['bkName']
    list_filter = ['bkName', 'authorName','price']
    search_fields = ['bkName']
    list_editable = ['authorName','publisher','pubversion','price']
    class Meta:
        model = Book

admin.site.register(Book,CommentModelAdmin)