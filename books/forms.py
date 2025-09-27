from django import forms
from .models import Book, BookCategory, ExpenseUpload

class BookCategoryForm(forms.ModelForm):
    class Meta:
        model = BookCategory
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_id', 'title', 'subtitle', 'authors', 'publisher', 
                 'published_date', 'category', 'distribution_expense']
        widgets = {
            'book_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ISBN or Book ID'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Optional'}),
            'authors': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comma-separated if multiple'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control'}),
            'published_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'distribution_expense': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
        }

class ExpenseUploadForm(forms.ModelForm):
    class Meta:
        model = ExpenseUpload
        fields = ['file']
        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-control', 'accept': '.xlsx,.xls,.csv'}),
        }