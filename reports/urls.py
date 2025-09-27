from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('expense-breakdown/', views.expense_breakdown, name='expense_breakdown'),
    path('forecast/', views.forecast_expenses, name='forecast_expenses'),
]