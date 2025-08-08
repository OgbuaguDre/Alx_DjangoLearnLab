from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

# ListView – retrieve all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # anyone can view list
    
    # Enable filtering, search, and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    # Step 1: Filtering by specific fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Step 2: Searching by text match
    search_fields = ['title', 'author']

    # Step 3: Ordering by certain fields
    ordering_fields = ['title', 'publication_year']

    # Default ordering
    ordering = ['title']

# DetailView – retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # anyone can view details


# CreateView – add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # must be logged in
    def perform_create(self, serializer):
        # Automatically set the user who created the book
        serializer.save(created_by=self.request.user)


# UpdateView – modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # must be logged in
     def perform_update(self, serializer):
        # Prevent title from being blank
        if not serializer.validated_data.get("title"):
            raise serializers.ValidationError({"title": "Title cannot be blank"})
        serializer.save()


# DeleteView – remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # must be logged in

# Create your views here.




