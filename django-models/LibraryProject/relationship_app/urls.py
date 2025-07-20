# relationship_app/urls.py

from django.urls import path
from .views import BookDetailView, LibraryListView  # Replace with your actual views

urlpatterns = [
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('libraries/', LibraryListView.as_view(), name='library-list'),
]
