# relationship_app/urls.py
from .views import list_books, LibraryDetailView

from django.urls import path
from .views import BookDetailView, LibraryListView  # Replace with your actual views
from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # your own views (e.g., for registration)
from django.urls import path
from . import views

urlpatterns = [
    path('admin-role/', views.admin_view, name='admin_view'),
    path('librarian-role/', views.librarian_view, name='librarian_view'),
    path('member-role/', views.member_view, name='member_view'),
]

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    # Add any additional views, e.g. home/list_books
]

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
