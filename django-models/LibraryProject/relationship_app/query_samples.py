import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return author.books.all()

# Query 2: List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

# Sample usage
if __name__ == "__main__":
    print("Books by 'Chinua Achebe':", get_books_by_author('Chinua Achebe'))
    print("Books in 'Central Library':", get_books_in_library('Central Library'))
    print("Librarian for 'Central Library':", get_librarian_for_library('Central Library'))
