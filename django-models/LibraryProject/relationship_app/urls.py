# relationship_app/urls.py
from .views import list_books, LibraryDetailView

from django.urls import path
from .views import BookDetailView, LibraryListView  # Replace with your actual views
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    # your previous routes like:
    # path('books/', views.list_books, name='list_books'),
    # path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

urlpatterns = [
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('libraries/', LibraryListView.as_view(), name='library-list'),
]
