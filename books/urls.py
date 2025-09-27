from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('books/', views.book_list, name='book_list'),
    path('import/', views.import_data, name='import_data'),
]