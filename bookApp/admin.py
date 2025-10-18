from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(BooksModel)
class BooksAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "isbn", "available_copies"]

@admin.register(AuthorsModel)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ["name", "nationality", "is_alive"]

@admin.register(BorrowRecordsModel)
class BorrowRecordsAdmin(admin.ModelAdmin):
    list_display = ["book_title", "borrower_name", "borrow_date", "due_date", "is_returned"]

    def book_title(self, obj):
        return obj.book.title

    book_title.short_description = 'Book'

    def borrower_name(self, obj):
        return obj.borrower.name

    borrower_name.short_description = 'Borrower'