# for Django Admin customization
from django.contrib import admin
from .models import Book, BookCategory, ExpenseUpload

@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'category', 'published_date', 'distribution_expense')
    list_filter = ('category', 'published_date', 'publisher')
    search_fields = ('title', 'authors', 'publisher')
    ordering = ('-published_date',)

@admin.register(ExpenseUpload)
class ExpenseUploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'uploaded_at', 'processed')
    list_filter = ('processed', 'uploaded_at')