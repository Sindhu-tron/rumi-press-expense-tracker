# reports/views.py - REPLACE ENTIRE FILE
from django.shortcuts import render
from django.db.models import Sum, Count, Avg
from books.models import Book, BookCategory

def dashboard(request):
    # Basic statistics
    total_books = Book.objects.count()
    total_categories = BookCategory.objects.count()
    total_expenses = Book.objects.aggregate(
        total=Sum('distribution_expense')
    )['total'] or 0
    
    # Category-wise data with proper averages
    category_data = BookCategory.objects.annotate(
        book_count=Count('books'),
        total_expense=Sum('books__distribution_expense'),
        avg_expense=Avg('books__distribution_expense')  # This calculates average automatically
    ).filter(book_count__gt=0).order_by('-total_expense')
    
    context = {
        'total_books': total_books,
        'total_categories': total_categories, 
        'total_expenses': total_expenses,
        'category_data': category_data,
    }
    
    return render(request, 'reports/dashboard.html', context)

def expense_breakdown(request):
    category_data = BookCategory.objects.annotate(
        book_count=Count('books'),
        total_expense=Sum('books__distribution_expense'),
        avg_expense=Avg('books__distribution_expense')
    ).filter(book_count__gt=0).order_by('-total_expense')
    
    context = {
        'category_data': category_data,
    }
    return render(request, 'reports/expense_breakdown.html', context)

def forecast_expenses(request):
    return render(request, 'reports/forecast.html')