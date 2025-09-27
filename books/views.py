# books/views.py - COMPLETE FILE WITH IMPORT PROCESSING
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import BookCategory, Book
import pandas as pd
from datetime import datetime

def category_list(request):
    categories = BookCategory.objects.all()
    return render(request, 'books/category_list.html', {
        'categories': categories
    })

def book_list(request):
    books = Book.objects.select_related('category').all()
    return render(request, 'books/book_list.html', {
        'books': books
    })

# Update the import_data function in books/views.py
# Update your import_data function in books/views.py
def import_data(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        
        try:
            df = pd.read_excel(uploaded_file)
            
            def clean_category(category):
                if pd.isna(category) or str(category).lower() == 'undefined':
                    return 'Uncategorized'
                
                category = str(category).strip()
                category_mapping = {
                    'python': 'Python',
                    'nlp': 'NLP', 
                    'r studio': 'R Studio',
                    'sql': 'SQL',
                    'deep learning': 'Deep Learning',
                    'data science': 'Data Science',
                    'data ethics': 'Data Ethics',
                    'business analytics': 'Business Analytics',
                    'maths': 'Mathematics',
                    'statistics': 'Statistics',
                    'visualization': 'Visualization'
                }
                
                return category_mapping.get(category.lower(), category.title())
            
            def convert_excel_date(excel_date):
                # Handle the problematic date format
                if pd.isna(excel_date):
                    return datetime(2023, 1, 1).date()
                
                # Check for Excel display errors (### symbols)
                if isinstance(excel_date, str) and '#' in str(excel_date):
                    return datetime(2023, 1, 1).date()
                
                if isinstance(excel_date, (int, float)):
                    if excel_date > 59:
                        excel_date -= 1
                    base_date = pd.to_datetime('1899-12-30')
                    return (base_date + pd.Timedelta(days=excel_date)).date()
                else:
                    return pd.to_datetime(excel_date).date()
            
            successful_imports = 0
            error_count = 0
            error_details = []
            
            messages.info(request, f'Processing {len(df)} rows from Excel file...')
            
            # Pre-create categories
            unique_categories = df['category'].dropna().unique()
            category_objects = {}
            
            for cat_name in unique_categories:
                clean_name = clean_category(cat_name)
                category, created = BookCategory.objects.get_or_create(
                    name=clean_name,
                    defaults={'description': f'Books in {clean_name} category'}
                )
                category_objects[cat_name] = category
            
            # Process each row with unique book_id
            for index, row in df.iterrows():
                try:
                    # Skip rows with critical missing data
                    if pd.isna(row['title']) or pd.isna(row['authors']):
                        error_count += 1
                        continue
                    
                    # Create unique book_id using row index + original ID
                    try:
                        original_id = str(row['id']).strip()
                        # Combine row index with original ID for uniqueness
                        book_id = int(f"{index}{abs(hash(original_id)) % 100000}")
                    except:
                        # Fallback: use row index
                        book_id = 1000000 + index
                    
                    # Get category
                    category = category_objects.get(row['category'])
                    if not category:
                        # Use first available category as fallback
                        category = list(category_objects.values())[0]
                    
                    # Convert date with error handling
                    try:
                        pub_date = convert_excel_date(row['published_date'])
                    except:
                        pub_date = datetime(2023, 1, 1).date()
                    
                    # Create book (each row gets a unique ID)
                    Book.objects.create(
                        book_id=book_id,
                        title=str(row['title'])[:300],
                        subtitle=str(row.get('subtitle', ''))[:300] if pd.notna(row.get('subtitle')) else None,
                        authors=str(row['authors'])[:200],
                        publisher=str(row.get('publisher', 'Unknown'))[:200],
                        published_date=pub_date,
                        category=category,
                        distribution_expense=float(row['distribution_expense']),
                    )
                    
                    successful_imports += 1
                    
                    if successful_imports % 500 == 0:
                        messages.info(request, f'Processed {successful_imports} books...')
                    
                except Exception as row_error:
                    error_count += 1
                    if len(error_details) < 10:
                        error_details.append(f"Row {index + 1}: {str(row_error)}")
            
            final_count = Book.objects.count()
            messages.success(
                request, 
                f'Import completed! {successful_imports} books created. '
                f'Database now contains {final_count} books total.'
            )
            
            if error_count > 0:
                messages.warning(request, f'{error_count} rows had errors.')
            
            return redirect('dashboard')
            
        except Exception as e:
            messages.error(request, f'Error reading file: {str(e)}')
            
    return render(request, 'books/import_data.html')