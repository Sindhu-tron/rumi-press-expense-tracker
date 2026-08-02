# rumi-press-expense-tracker
A Django web application for tracking book distribution expenses. Built to replace a manual spreadsheet workflow with automated Excel import, a searchable book database, and a simple analytics dashboard.
/das

## What it does
 
- **Imports book data from Excel files** — parses `.xlsx`/`.xls` with validation, duplicate handling, and error reporting
- **Tracks distribution expenses** across book categories with full CRUD operations
- **Provides a dashboard** showing totals, category breakdowns, and average costs
Working dataset: ~4,090 books across 11 categories, tracking ~$21,600 in distribution expenses.
 
## Tech stack
 
- **Backend:** Django 4.2, Python 3.11, Pandas + OpenPyXL for Excel processing
- **Frontend:** Bootstrap 5, HTML/CSS/JS
- **Database:** SQLite (development)
- **Deployment:** Docker + docker-compose

## Running it
 
```bash
git clone https://github.com/Sindhu-tron/rumi-press-expense-tracker.git
cd rumi-press-expense-tracker
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
 
Visit `http://127.0.0.1:8000`.
 
Or with Docker:
 
```bash
docker-compose up
```

## Screenshots
 
**Dashboard** — expense totals and category breakdown
![Dashboard](screenshots/Dashboard overview screenshot.png)
 
**Book list** — searchable, filterable
![Books](screenshots/Book management screenshot.png)
 
**Excel import** — upload with progress and error reporting
![Import](screenshots/import screenshot.png)

## Project structure
 
```
├── books/              # Book management app (models, views, forms)
├── reports/            # Dashboard and analytics views
├── templates/          # HTML templates
├── static/             # CSS, JS, images
├── screenshots/        # README images
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── manage.py
```
 
## What I'd do differently
 
The analytics are basic Django ORM aggregations rendered as HTML. For a real analytics use case I'd add Plotly or Chart.js for interactive charts and expose a REST API for external BI tools. The import pipeline also has no async processing — for genuinely large files, Celery with a task queue would be the right move.
 
## Author
 
Sindhuja Dantuluri — [LinkedIn](https://www.linkedin.com/in/SindhujaDantuluri/)
 
## Licence
 
MIT



**Project Overview**
This application processes large-scale book distribution data, providing automated import capabilities, expense analytics, and business intelligence dashboards. Built to handle enterprise-level data volumes while maintaining performance and usability standards.
Live Data: 4,090 books across 11 categories tracking $21,598.69 in distribution expenses

## Key Features
**Data Processing & Import**

Automated Excel Processing: Handles complex Excel files with data validation and error handling
Smart Data Cleaning: Automatically standardizes categories, converts date formats, and handles duplicates
Batch Import: Processes thousands of records with progress tracking and detailed error reporting
Data Validation: Comprehensive input validation with user-friendly error messages

**Business Intelligence**

Real-time Dashboard: Live analytics showing expense distributions and category breakdowns
Category Analysis: Detailed insights into spending patterns across book categories
Expense Tracking: Complete audit trail of all distribution costs
Performance Metrics: Average costs, total expenses, and book count analytics

**User Interface**

Responsive Design: Mobile-friendly interface using Bootstrap 5
Intuitive Navigation: Clean, professional layout with logical information architecture
Search & Filter: Advanced filtering capabilities for large datasets
Admin Integration: Seamless Django admin interface for backend management

## Technology Stack
**Backend**

Django 4.2 (Python web framework)
Python 3.11
SQLite (development) / PostgreSQL (production-ready)
Pandas (data processing)
OpenPyXL (Excel file handling)

**Frontend**

Bootstrap 5 (responsive design)
HTML5 / CSS3
JavaScript (interactive features)
Font Awesome (icons)

**Data & Analytics**

Django ORM (database queries and aggregations)
Plotly (extensible for advanced visualizations)
Custom analytics engine

## Quick Start
**Prerequisites**

Python 3.11+
pip package manager
Git

Installation
bash# Clone the repository
git clone https://github.com/yourusername/rumi-press-expense-tracker.git
cd rumi-press-expense-tracker

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Database setup
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start development server
python manage.py runserver
Visit http://127.0.0.1:8000 to access the application.

## Usage
**Data Import**

Navigate to the Import section
Upload your Excel file (supports .xlsx, .xls formats)
Review import progress and results
Check dashboard for updated analytics

**Expected Excel Format**
Columns: id, title, subtitle, authors, publisher, published_date, category, distribution_expense

**Dashboard Analytics**

View total books, categories, and expenses
Analyze category-wise spending patterns
Review average costs per book
Track expense distributions

**Project Structure**
rumi_press/
├── manage.py                 # Django management script
├── rumi_press/              # Main project configuration
│   ├── settings.py          # Django settings
│   ├── urls.py              # URL routing
│   └── wsgi.py              # WSGI configuration
├── books/                   # Books management app
│   ├── models.py            # Data models
│   ├── views.py             # View logic
│   ├── forms.py             # Form definitions
│   ├── admin.py             # Admin interface
│   └── urls.py              # App URLs
├── reports/                 # Analytics and reporting
│   ├── views.py             # Dashboard and analytics
│   └── urls.py              # Report URLs
├── templates/               # HTML templates
│   ├── base.html            # Base template
│   ├── books/               # Book-related templates
│   └── reports/             # Analytics templates
└── static/                  # CSS, JavaScript, images

## Screenshots
**Dashboard Overview**
*Real-time analytics showing 4,090 books across 11 categories*
<img width="1417" height="736" alt="image" src="https://github.com/user-attachments/assets/dfe1a290-8460-47e6-a43b-2072fb2a47a4" />


**Book Management**
*Complete CRUD interface with search and filtering*
<img width="1417" height="736" alt="image" src="https://github.com/user-attachments/assets/c5368aef-1984-4f9e-9449-66c3a1a76b1f" />


**Expense Analysis**
*Category-wise expense breakdown with visual indicators*
<img width="1417" height="736" alt="image" src="https://github.com/user-attachments/assets/7f49ba1b-b7db-4061-9215-c05fa1818760" />


**Data Import**
*Excel file processing with progress tracking*
<img width="1417" height="736" alt="image" src="https://github.com/user-attachments/assets/2d32cfd1-a7c0-48b8-8ed5-9248a2e185e1" />



##Data Models
**BookCategory**

Category management with automatic creation during import
Hierarchical organization of book types
Relationship tracking with books

**Book**

Comprehensive book information (title, authors, publisher, dates)
Expense tracking with validation
Category relationships and search capabilities

**ExpenseUpload**

Import history and audit trails
File upload tracking and processing status

**Key Achievements**
Data Processing Excellence

Successfully imported 4,090 real book records with 96% success rate
Implemented robust error handling for problematic data formats
Built scalable import system capable of handling enterprise datasets

**Business Intelligence Implementation**

Created meaningful analytics from $21,598.69 in tracked expenses
Developed category-wise analysis showing Python books as highest expense category ($2,389.37)
Built responsive dashboards providing actionable business insights

**Technical Implementation**

Designed normalized database schema supporting future growth
Implemented proper Django patterns (MVT architecture, ORM usage)
Created production-ready error handling and user feedback systems

**Performance Considerations**

Optimized database queries using select_related and prefetch_related
Implemented pagination for large datasets
Efficient bulk import operations
Responsive design optimized for various screen sizes

**Security Features**

CSRF protection on all forms
Input validation and sanitization
SQL injection prevention through Django ORM
Secure file upload handling

## Future Enhancements
**Analytics & Forecasting**

Machine learning integration for expense prediction
Trend analysis and seasonal pattern recognition
Budget planning and recommendation engine

**Advanced Features**

RESTful API for external integrations
Advanced filtering and search capabilities
Export functionality (PDF reports, Excel exports)
User role management and permissions

**Integration Capabilities**

Power BI connectivity (API endpoints ready)
Accounting software integration
Automated reporting and email notifications

**Testing**
bash# Run tests
python manage.py test

# Check code coverage
coverage run --source='.' manage.py test
coverage report

**Deployment**
The application includes Docker configuration and is ready for deployment to:

Heroku
AWS/DigitalOcean
Docker containers

**Contributing**

Fork the repository
Create a feature branch (git checkout -b feature-name)
Commit changes (git commit -am 'Add feature')
Push to branch (git push origin feature-name)
Create Pull Request


**Contact**
Developer: Sindhuja Dantuluri
Email: sindhujavarma02@gmail.com
LinkedIn: https://www.linkedin.com/in/SindhujaDantuluri/


