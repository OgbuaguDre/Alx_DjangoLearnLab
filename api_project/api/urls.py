from django.urls import path
from .views import BookList
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

# Create a DRF router instance
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Old ListAPIView
    path('books/', BookList.as_view(), name='book-list'),

    # DRF router-generated CRUD routes
    path('', include(router.urls)),
]

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('token/', obtain_auth_token, name='api_token_auth'),  # Token endpoint
    path('', include(router.urls)),
]
