from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class BookCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Book Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Book(models.Model):
    book_id = models.BigIntegerField(unique=True, help_text="ISBN or Book ID from original data")
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    authors = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    published_date = models.DateField()
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, related_name='books')
    distribution_expense = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.00'))],
        help_text="Total distribution cost for this book"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-published_date']
    
    def __str__(self):
        return f"{self.title} by {self.authors}"

class ExpenseUpload(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Upload {self.id} - {self.uploaded_at}"